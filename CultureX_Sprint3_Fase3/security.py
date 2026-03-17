# CultureX Sprint 3 - Cybersecurity & Data Validation Layer
# Professional data integrity and security implementation

import logging
import time
import json
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class ValidationResult:
    """Result of data validation process"""
    is_valid: bool
    errors: List[str]
    warnings: List[str]
    cleaned_data: Optional[Dict[str, Any]] = None

class DataValidator:
    """Professional data validation with cybersecurity principles"""
    
    def __init__(self, config):
        self.config = config
        self.request_history = {}
        
    def validate_sensor_data(self, data: Dict[str, Any]) -> ValidationResult:
        """Comprehensive sensor data validation"""
        errors = []
        warnings = []
        cleaned_data = data.copy()
        
        # Schema validation
        required_fields = ['sensor_id', 'sensor_type', 'value', 'timestamp', 'location']
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing required field: {field}")
        
        if errors:
            return ValidationResult(False, errors, warnings)
        
        # Sensor ID validation
        if data['sensor_id'] not in self.config.seguranca.ids_sensores_permitidos:
            errors.append(f"ID de sensor não autorizado: {data['sensor_id']}")
        
        # Value range validation
        sensor_type = data['sensor_type']
        value = data['value']
        
        if sensor_type == 'temperature':
            if not (self.config.sensores.temperatura_minima <= value <= self.config.sensores.temperatura_maxima):
                errors.append(f"Temperatura fora da faixa: {value}")
        
        elif sensor_type == 'humidity':
            if not (self.config.sensores.umidade_minima <= value <= self.config.sensores.umidade_maxima):
                errors.append(f"Umidade fora da faixa: {value}")
        
        elif sensor_type == 'proximity':
            if not (0 <= value <= 500):
                errors.append(f"Proximity out of range: {value}cm")
        
        # Timestamp validation
        try:
            timestamp = pd.to_datetime(data['timestamp'])
            now = datetime.now()
            if timestamp > now + timedelta(minutes=5):
                warnings.append("Future timestamp detected")
            elif timestamp < now - timedelta(hours=24):
                warnings.append("Very old timestamp detected")
        except:
            errors.append("Invalid timestamp format")
        
        # Rate limiting
        if not self._check_rate_limit(data['sensor_id']):
            errors.append("Rate limit exceeded for sensor")
        
        # Data sanitization
        cleaned_data = self._sanitize_data(cleaned_data)
        
        is_valid = len(errors) == 0
        
        if is_valid:
            logger.info(f"Data validation passed for {data['sensor_id']}")
        else:
            logger.warning(f"Data validation failed: {errors}")
        
        return ValidationResult(is_valid, errors, warnings, cleaned_data)
    
    def _check_rate_limit(self, sensor_id: str) -> bool:
        """Check if sensor is within rate limits"""
        now = time.time()
        minute_ago = now - 60
        
        if sensor_id not in self.request_history:
            self.request_history[sensor_id] = []
        
        # Clean old requests
        self.request_history[sensor_id] = [
            req_time for req_time in self.request_history[sensor_id] 
            if req_time > minute_ago
        ]
        
        # Check rate limit
        if len(self.request_history[sensor_id]) >= self.config.seguranca.taxa_maxima_requisicoes:
            return False
        
        # Add current request
        self.request_history[sensor_id].append(now)
        return True
    
    def _sanitize_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Sanitize data for security"""
        sanitized = {}
        
        for key, value in data.items():
            if isinstance(value, str):
                # Remove potential SQL injection characters
                sanitized[key] = value.replace("'", "").replace(";", "").replace("--", "")
            else:
                sanitized[key] = value
        
        return sanitized

class DatabaseIntegrityChecker:
    """Database integrity and consistency checker"""
    
    def __init__(self, connection):
        self.connection = connection
    
    def check_data_integrity(self) -> Dict[str, Any]:
        """Comprehensive database integrity check"""
        results = {
            'total_records': 0,
            'null_values': {},
            'duplicate_records': 0,
            'data_quality_score': 0.0,
            'consistency_issues': []
        }
        
        try:
            # Check sensor_data table
            sensor_df = pd.read_sql_query("SELECT * FROM sensor_data", self.connection)
            results['total_records'] = len(sensor_df)
            
            # Check for null values
            for column in sensor_df.columns:
                null_count = sensor_df[column].isnull().sum()
                if null_count > 0:
                    results['null_values'][column] = null_count
            
            # Check for duplicates
            duplicates = sensor_df.duplicated().sum()
            results['duplicate_records'] = duplicates
            
            # Check for data consistency
            if 'timestamp' in sensor_df.columns:
                future_timestamps = sensor_df[
                    pd.to_datetime(sensor_df['timestamp']) > datetime.now()
                ]
                if len(future_timestamps) > 0:
                    results['consistency_issues'].append(f"{len(future_timestamps)} future timestamps found")
            
            # Calculate data quality score
            total_issues = sum(results['null_values'].values()) + duplicates + len(results['consistency_issues'])
            results['data_quality_score'] = max(0, 100 - (total_issues / max(results['total_records'], 1)) * 100)
            
            logger.info(f"Database integrity check completed. Quality score: {results['data_quality_score']:.2f}%")
            
        except Exception as e:
            logger.error(f"Database integrity check failed: {e}")
            results['error'] = str(e)
        
        return results

class SecurityMonitor:
    """Real-time security monitoring"""
    
    def __init__(self):
        self.security_events = []
        self.threat_level = "LOW"
    
    def log_security_event(self, event_type: str, details: Dict[str, Any]):
        """Log security events for monitoring"""
        event = {
            'timestamp': datetime.now(),
            'type': event_type,
            'details': details,
            'severity': self._calculate_severity(event_type)
        }
        
        self.security_events.append(event)
        self._update_threat_level()
        
        logger.warning(f"Security event: {event_type} - {details}")
    
    def _calculate_severity(self, event_type: str) -> str:
        """Calculate event severity"""
        high_severity_events = ['unauthorized_access', 'data_injection', 'rate_limit_exceeded']
        medium_severity_events = ['invalid_data', 'suspicious_pattern']
        
        if event_type in high_severity_events:
            return "HIGH"
        elif event_type in medium_severity_events:
            return "MEDIUM"
        else:
            return "LOW"
    
    def _update_threat_level(self):
        """Update overall system threat level"""
        recent_events = [
            event for event in self.security_events 
            if event['timestamp'] > datetime.now() - timedelta(hours=1)
        ]
        
        high_severity_count = sum(1 for event in recent_events if event['severity'] == 'HIGH')
        
        if high_severity_count >= 5:
            self.threat_level = "CRITICAL"
        elif high_severity_count >= 2:
            self.threat_level = "HIGH"
        elif len(recent_events) >= 10:
            self.threat_level = "MEDIUM"
        else:
            self.threat_level = "LOW"
    
    def get_security_report(self) -> Dict[str, Any]:
        """Generate security monitoring report"""
        recent_events = [
            event for event in self.security_events 
            if event['timestamp'] > datetime.now() - timedelta(hours=24)
        ]
        
        event_types = {}
        severity_dist = {}
        
        for event in recent_events:
            event_type = event['type']
            severity = event['severity']
            
            event_types[event_type] = event_types.get(event_type, 0) + 1
            severity_dist[severity] = severity_dist.get(severity, 0) + 1
        
        return {
            'current_threat_level': self.threat_level,
            'events_last_24h': len(recent_events),
            'event_types': event_types,
            'severity_distribution': severity_dist
        }

def initialize_security_layer(config):
    """Inicializar componentes de segurança"""
    validator = DataValidator(config)
    security_monitor = SecurityMonitor()
    logger.info("Camada de segurança inicializada com sucesso")
    return validator, security_monitor