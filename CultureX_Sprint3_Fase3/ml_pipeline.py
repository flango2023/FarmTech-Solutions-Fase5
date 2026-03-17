# CultureX Sprint 3 - Enhanced ML Pipeline
# Machine Learning with comprehensive evaluation metrics

import numpy as np
import pandas as pd
import logging
from typing import Dict, List, Tuple, Any, Optional
from datetime import datetime
from dataclasses import dataclass

# ML imports
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    mean_absolute_error, mean_squared_error, r2_score,
    confusion_matrix
)
from sklearn.cluster import KMeans
import joblib
import warnings
warnings.filterwarnings('ignore')

logger = logging.getLogger(__name__)

@dataclass
class MLMetrics:
    """ML model evaluation metrics"""
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    mae: Optional[float] = None
    rmse: Optional[float] = None
    r2_score: Optional[float] = None
    cross_val_score: Optional[float] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if v is not None}

class EnhancedMLPipeline:
    """Professional ML pipeline with comprehensive evaluation"""
    
    def __init__(self, config):
        self.config = config
        self.models = {}
        self.scalers = {}
        self.encoders = {}
        
    def prepare_features(self, df: pd.DataFrame) -> np.ndarray:
        """Feature engineering for ML models"""
        if df.empty:
            return np.array([])
        
        features = []
        
        # Time-based features
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df['hour'] = df['timestamp'].dt.hour
            df['day_of_week'] = df['timestamp'].dt.dayofweek
            df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
        
        # Location encoding
        if 'location' in df.columns:
            location_encoder = LabelEncoder()
            df['location_encoded'] = location_encoder.fit_transform(df['location'])
            self.encoders['location'] = location_encoder
        
        # Select numeric features
        feature_columns = []
        for col in ['value', 'hour', 'day_of_week', 'is_weekend', 'location_encoded']:
            if col in df.columns:
                feature_columns.append(col)
        
        if feature_columns:
            X = df[feature_columns].fillna(0)
            return X.values
        else:
            return np.array([])
    
    def train_interaction_classifier(self, df: pd.DataFrame) -> MLMetrics:
        """Train interaction classification model"""
        logger.info("Training interaction classifier...")
        
        if df.empty or 'event_type' not in df.columns:
            logger.warning("Insufficient data for classification")
            return MLMetrics()
        
        X = self.prepare_features(df)
        y = df['event_type'].values
        
        if len(X) == 0 or len(np.unique(y)) < 2:
            logger.warning("Insufficient data for classification")
            return MLMetrics()
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self.config.ml.tamanho_teste, 
            random_state=self.config.ml.estado_aleatorio
        )
        
        # Scale features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        self.scalers['classifier'] = scaler
        
        # Train model
        rf = RandomForestClassifier(
            n_estimators=100,
            random_state=self.config.ml.estado_aleatorio
        )
        rf.fit(X_train_scaled, y_train)
        self.models['interaction_classifier'] = rf
        
        # Predictions
        y_pred = rf.predict(X_test_scaled)
        
        # Calculate metrics
        metrics = MLMetrics(
            accuracy=accuracy_score(y_test, y_pred),
            precision=precision_score(y_test, y_pred, average='weighted', zero_division=0),
            recall=recall_score(y_test, y_pred, average='weighted', zero_division=0),
            f1_score=f1_score(y_test, y_pred, average='weighted', zero_division=0),
            cross_val_score=cross_val_score(rf, X_train_scaled, y_train, cv=3).mean()
        )
        
        logger.info(f"Classifier trained - Accuracy: {metrics.accuracy:.3f}")
        return metrics
    
    def train_visitor_flow_predictor(self, df: pd.DataFrame) -> MLMetrics:
        """Train visitor flow prediction model"""
        logger.info("Training visitor flow predictor...")
        
        if df.empty:
            logger.warning("No data for regression")
            return MLMetrics()
        
        # Aggregate hourly data
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        hourly_data = df.groupby(df['timestamp'].dt.floor('H')).agg({
            'value': 'count',
            'location': 'nunique'
        }).reset_index()
        
        hourly_data.columns = ['timestamp', 'visitor_count', 'location_count']
        hourly_data['hour'] = hourly_data['timestamp'].dt.hour
        hourly_data['day_of_week'] = hourly_data['timestamp'].dt.dayofweek
        
        if len(hourly_data) < 10:
            logger.warning("Insufficient data for regression")
            return MLMetrics()
        
        # Prepare features
        X = hourly_data[['hour', 'day_of_week', 'location_count']].values
        y = hourly_data['visitor_count'].values
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self.config.ml.tamanho_teste, 
            random_state=self.config.ml.estado_aleatorio
        )
        
        # Scale features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        self.scalers['regressor'] = scaler
        
        # Train model
        rf_regressor = RandomForestRegressor(
            n_estimators=100,
            random_state=self.config.ml.estado_aleatorio
        )
        rf_regressor.fit(X_train_scaled, y_train)
        self.models['flow_predictor'] = rf_regressor
        
        # Predictions
        y_pred = rf_regressor.predict(X_test_scaled)
        
        # Calculate metrics
        metrics = MLMetrics(
            mae=mean_absolute_error(y_test, y_pred),
            rmse=np.sqrt(mean_squared_error(y_test, y_pred)),
            r2_score=r2_score(y_test, y_pred),
            cross_val_score=cross_val_score(rf_regressor, X_train_scaled, y_train, cv=3).mean()
        )
        
        logger.info(f"Regressor trained - MAE: {metrics.mae:.3f}")
        return metrics
    
    def perform_behavioral_clustering(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Behavioral clustering analysis"""
        logger.info("Performing behavioral clustering...")
        
        if df.empty:
            return {'error': 'No data for clustering'}
        
        # Aggregate session features
        session_features = df.groupby('location').agg({
            'value': ['count', 'mean'],
            'sensor_type': 'nunique'
        }).reset_index()
        
        session_features.columns = ['location', 'interaction_count', 'avg_intensity', 'sensor_diversity']
        session_features = session_features.fillna(0)
        
        if len(session_features) < 3:
            return {'error': 'Insufficient data for clustering'}
        
        # Prepare features
        X = session_features[['interaction_count', 'avg_intensity', 'sensor_diversity']].values
        
        # Scale features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Clustering
        n_clusters = min(3, len(X))
        kmeans = KMeans(n_clusters=n_clusters, random_state=self.config.ml.estado_aleatorio)
        clusters = kmeans.fit_predict(X_scaled)
        
        # Analyze clusters
        session_features['cluster'] = clusters
        cluster_analysis = {}
        
        for cluster_id in range(n_clusters):
            cluster_data = session_features[session_features['cluster'] == cluster_id]
            cluster_analysis[f'cluster_{cluster_id}'] = {
                'size': len(cluster_data),
                'avg_interactions': float(cluster_data['interaction_count'].mean()),
                'avg_intensity': float(cluster_data['avg_intensity'].mean()),
                'behavior_type': self._classify_behavior_type(cluster_data)
            }
        
        return {
            'optimal_clusters': n_clusters,
            'cluster_analysis': cluster_analysis
        }
    
    def _classify_behavior_type(self, cluster_data: pd.DataFrame) -> str:
        """Classify behavior type based on cluster characteristics"""
        avg_interactions = cluster_data['interaction_count'].mean()
        avg_intensity = cluster_data['avg_intensity'].mean()
        
        if avg_interactions > 10 and avg_intensity > 0.7:
            return "High Engagement"
        elif avg_interactions > 5 and avg_intensity > 0.5:
            return "Moderate Engagement"
        elif avg_interactions < 3:
            return "Casual Visitor"
        else:
            return "Standard Visitor"
    
    def save_models(self, model_dir: str = "models/"):
        """Save trained models"""
        import os
        os.makedirs(model_dir, exist_ok=True)
        
        for name, model in self.models.items():
            joblib.dump(model, f"{model_dir}/{name}.pkl")
        
        for name, scaler in self.scalers.items():
            joblib.dump(scaler, f"{model_dir}/scaler_{name}.pkl")
        
        for name, encoder in self.encoders.items():
            joblib.dump(encoder, f"{model_dir}/encoder_{name}.pkl")
        
        logger.info(f"Models saved to {model_dir}")
    
    def load_models(self, model_dir: str = "models/"):
        """Load saved models"""
        import os
        
        try:
            for filename in os.listdir(model_dir):
                if filename.endswith('.pkl'):
                    if filename.startswith('scaler_'):
                        name = filename.replace('scaler_', '').replace('.pkl', '')
                        self.scalers[name] = joblib.load(f"{model_dir}/{filename}")
                    elif filename.startswith('encoder_'):
                        name = filename.replace('encoder_', '').replace('.pkl', '')
                        self.encoders[name] = joblib.load(f"{model_dir}/{filename}")
                    else:
                        name = filename.replace('.pkl', '')
                        self.models[name] = joblib.load(f"{model_dir}/{filename}")
            
            logger.info("Models loaded successfully")
            
        except Exception as e:
            logger.error(f"Error loading models: {e}")

def calculate_ml_metrics(y_true, y_pred, model_type='classification'):
    """Calculate ML metrics for technical reports"""
    
    if model_type == 'classification':
        metrics = {
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, average='weighted', zero_division=0),
            'recall': recall_score(y_true, y_pred, average='weighted', zero_division=0),
            'f1_score': f1_score(y_true, y_pred, average='weighted', zero_division=0)
        }
        
        cm = confusion_matrix(y_true, y_pred)
        metrics['confusion_matrix'] = cm.tolist()
        
    else:  # regression
        metrics = {
            'mae': mean_absolute_error(y_true, y_pred),
            'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
            'r2_score': r2_score(y_true, y_pred)
        }
        
        residuals = y_true - y_pred
        metrics['residual_stats'] = {
            'mean': float(np.mean(residuals)),
            'std': float(np.std(residuals)),
            'min': float(np.min(residuals)),
            'max': float(np.max(residuals))
        }
    
    return metrics