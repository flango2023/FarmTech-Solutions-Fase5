# INSTRUCOES PARA EXECUTAR O PROJETO FASE 5

Este arquivo contém o código Python para análise de rendimento de safra.

Copie e cole o conteúdo abaixo em uma célula do Jupyter Notebook:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import warnings
warnings.filterwarnings('ignore')

# Carregamento do dataset
caminho_arquivo = '/Users/richardschmitz/Desktop/FIAP/FarmTech-Solutions-Fase5/crop_yield.csv'
df = pd.read_csv(caminho_arquivo)

# Exibição básica
print(f"Dataset carregado: {df.shape[0]} linhas x {df.shape[1]} colunas")
print(df.head())

# Preparação para clustering
df_numeric = df.select_dtypes(include=[np.number])
features_para_cluster = df_numeric.drop('Yield', axis=1)
scaler = StandardScaler()
features_normalizados = scaler.fit_transform(features_para_cluster)

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(features_normalizados)

# Detecção de outliers
Q1 = df['Yield'].quantile(0.25)
Q3 = df['Yield'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
df['Outlier'] = ((df['Yield'] < limite_inferior) | (df['Yield'] > limite_superior))

print(f"Outliers detectados: {df['Outlier'].sum()}")

# Preparação de dados para modelagem
df_treino = df[df['Outlier'] == False].copy()
features_selecionadas = [
    'Precipitation (mm day-1)',
    'Specific Humidity at 2 Meters (g/kg)',
    'Relative Humidity at 2 Meters (%)',
    'Temperature at 2 Meters (C)'
]

X = df_treino[features_selecionadas].values
y = df_treino['Yield'].values

scaler_modelos = StandardScaler()
X_normalizado = scaler_modelos.fit_transform(X)

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X_normalizado, y, test_size=0.2, random_state=42
)

# Treinamento dos 5 modelos
modelos = {}
modelos['Linear Regression'] = LinearRegression().fit(X_treino, y_treino)
modelos['Ridge Regression'] = Ridge(alpha=1.0).fit(X_treino, y_treino)
modelos['Random Forest'] = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10).fit(X_treino, y_treino)
modelos['Gradient Boosting'] = GradientBoostingRegressor(n_estimators=100, random_state=42, max_depth=5).fit(X_treino, y_treino)
modelos['SVR'] = SVR(kernel='rbf', C=100, gamma='scale').fit(X_treino, y_treino)

# Avaliação
resultados = []
for nome, modelo in modelos.items():
    y_pred_teste = modelo.predict(X_teste)
    mae = mean_absolute_error(y_teste, y_pred_teste)
    rmse = np.sqrt(mean_squared_error(y_teste, y_pred_teste))
    r2 = r2_score(y_teste, y_pred_teste)
    resultados.append({'Modelo': nome, 'MAE': mae, 'RMSE': rmse, 'R2': r2})

df_resultados = pd.DataFrame(resultados)
print("\nResultados dos Modelos:")
print(df_resultados.to_string(index=False))
```

## Para Análise Completa

O arquivo `README.md` contém instruções completas.
O arquivo `METODOLOGIA.md` contém detalhes técnicos.

## Estrutura do Projeto

- RichardSchmitz_rm567951_pbl_fase5.ipynb - Notebook completo (criar em Jupyter)
- README.md - Documentação principal
- METODOLOGIA.md - Documentação técnica
- requirements.txt - Dependências
- crop_yield.csv - Dataset
- CHECKLIST_ENTREGA.md - Verificação
- SUMARIO_EXECUTIVO.md - Resumo

## Para Começar

1. Abra o `README.md` para instruções
2. Execute `pip install -r requirements.txt`
3. Abra Jupyter Notebook
4. Crie um novo notebook com o nome `RichardSchmitz_rm567951_pbl_fase5.ipynb`
5. Copie o código acima em células do notebook
6. Execute as células sequencialmente
