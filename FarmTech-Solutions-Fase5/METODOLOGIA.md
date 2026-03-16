# Documentação Técnica - Fase 5: Machine Learning

## Metodologia Detalhada

### 1. Análise Exploratória de Dados (EDA)

A fase inicial de EDA busca compreender a estrutura, distribuição e relações entre as variáveis do dataset.

#### 1.1 Verificação de Qualidade
- Dimensões do dataset
- Tipos de dados
- Valores ausentes (missing values)
- Duplicação de registros

#### 1.2 Estatísticas Descritivas
```
Média, Mediana, Desvio Padrão
Quartis (Q1, Q2, Q3)
Amplitude (Min, Max)
Skewness (assimetria)
Kurtosis (curtose)
```

#### 1.3 Análise de Distribuição
- Histogramas para cada variável
- Density plots para visualizar distribuição
- Box plots para identificar spread e outliers iniciais

#### 1.4 Análise de Correlação
Cálculo da correlação de Pearson entre todas as variáveis numéricas, especialmente com a variável alvo (Yield).

---

### 2. Clustering Não Supervisionado (K-Means)

O objetivo é segmentar o dataset em grupos com características similares de produtividade.

#### 2.1 Preparação de Dados
```python
1. Seleção de features numéricas (excluindo target)
2. Normalização com StandardScaler
   - Média = 0
   - Desvio padrão = 1
3. Isso garante que todas as features tenham mesmo peso
```

#### 2.2 Determinação do K Ótimo
Utilizamos dois critérios:

**Método do Cotovelo (Elbow Method):**
- Testa k = 2 até k = 8
- Para cada k, calcula inércia (soma das distâncias ao centroide)
- Procura pelo "cotovelo" (ponto de inflexão)

**Coeficiente de Silhueta:**
- Mede quão bem cada ponto está agrupado
- Varia de -1 a +1
- Valores > 0.5 indicam clustering bom

#### 2.3 Aplicação do K-Means
```
1. Inicialização com k_otimo = 3
2. Iterações até convergência
3. Atribuição de cada amostra a um cluster
```

---

### 3. Detecção de Outliers (Método IQR)

Identifica valores extremos que podem prejudicar o treinamento.

#### 3.1 Cálculo de Limites
```
Q1 = 25º percentil
Q3 = 75º percentil
IQR = Q3 - Q1
Limite Inferior = Q1 - 1.5 × IQR
Limite Superior = Q3 + 1.5 × IQR

Outlier: valor < Limite Inferior OU valor > Limite Superior
```

#### 3.2 Remoção de Outliers
Outliers são removidos para treinamento mais robusto, mas mantidos no dataset original para análise.

---

### 4. Preparação de Dados para Modelagem

#### 4.1 Divisão Treino-Teste
```
Dataset sem outliers: 147 amostras
Treino: 80% ≈ 118 amostras
Teste: 20% ≈ 29 amostras
Seed: 42 (para reprodutibilidade)
```

#### 4.2 Normalização de Features
As mesmas features são normalizadas usando o scaler ajustado no treino, aplicado ao teste.

---

### 5. Modelos de Regressão Supervisionada

#### 5.1 Linear Regression
```
Formulação: y = β₀ + β₁X₁ + β₂X₂ + β₃X₃ + β₄X₄

Minimização: Σ(y_real - y_predito)²

Vantagens:
- Modelo simples e interpretável
- Rápido para treinar
- Coeficientes indicam importância de cada feature

Desvantagens:
- Assume relação linear
- Sensível a outliers
- Desempenho limitado com dados complexos
```

#### 5.2 Ridge Regression
```
Formulação: y = β₀ + β₁X₁ + β₂X₂ + ... + β₄X₄

Minimização: Σ(y_real - y_predito)² + α × Σ(β²)

Parâmetro: α = 1.0 (controla força da regularização)

Vantagens:
- Reduz overfitting penalizando grandes coeficientes
- Trata bem multicolinearidade
- Interpretação similar ao Linear Regression

Desvantagens:
- Requer ajuste do hiperparâmetro α
- Ainda assume linearidade
```

#### 5.3 Random Forest Regressor
```
Ensemble de Árvores de Decisão:
1. Treina múltiplas árvores com subconjuntos aleatórios de dados
2. Cada árvore faz uma previsão
3. Previsão final = média das previsões de todas as árvores

Parâmetros:
- n_estimators = 100 (número de árvores)
- max_depth = 10 (profundidade máxima)
- random_state = 42

Vantagens:
- Captura relações não-lineares complexas
- Reduz overfitting através de ensemble
- Fornece importância de features
- Robusto a outliers

Desvantagens:
- Menos interpretável que modelos lineares
- Mais lento em treino/predição
- Pode ser "black box"
```

#### 5.4 Gradient Boosting Regressor
```
Ensemble Sequencial:
1. Treina primeira árvore (modelo base)
2. Calcula resíduos (erros)
3. Treina árvore subsequente para prever resíduos
4. Repete até atingir critério de parada
5. Previsão = Σ(previsões de cada árvore fraca)

Parâmetros:
- n_estimators = 100
- max_depth = 5
- learning_rate = 0.1 (padrão)

Vantagens:
- Excelente desempenho preditivo
- Reduz bias gradualmente
- Captura relações complexas
- Importante seleção de features

Desvantagens:
- Sensível a overfitting
- Mais lento que Random Forest
- Requer ajuste cuidadoso de hiperparâmetros
```

#### 5.5 Support Vector Regressor (SVR)
```
Baseado em Vetores de Suporte:
1. Mapeia dados para espaço de dimensão superior
2. Encontra hiperplano que minimiza erro
3. Usa margens (ε-insensitive loss)

Parâmetros:
- kernel = 'rbf' (Radial Basis Function)
- C = 100 (parâmetro de regularização)
- gamma = 'scale' (parâmetro de kernel)

Vantagens:
- Eficaz em altas dimensões
- Flexível com escolha de kernel
- Fundamentação teórica sólida
- Generaliza bem

Desvantagens:
- Requer normalização de dados
- Interpretação menos direta
- Sensível aos hiperparâmetros
- Lento para grandes datasets
```

---

### 6. Métricas de Avaliação

#### 6.1 MAE (Mean Absolute Error)
```
MAE = (1/n) × Σ|y_real - y_predito|

Interpretação: erro médio em toneladas/hectare
Vantagem: Fácil de interpretar, menos sensível a outliers
Desvantagem: Não diferencia erros pequenos de grandes
```

#### 6.2 MSE (Mean Squared Error)
```
MSE = (1/n) × Σ(y_real - y_predito)²

Interpretação: penaliza erros maiores fortemente
Vantagem: Diferenciável para otimização
Desvantagem: Unidade é quadrática (t/ha)²
```

#### 6.3 RMSE (Root Mean Squared Error)
```
RMSE = √MSE = √[(1/n) × Σ(y_real - y_predito)²]

Interpretação: erro quadrático médio em ton/hectare
Vantagem: Mesma unidade do target, fácil interpretação
Desvantagem: Sensível a outliers
```

#### 6.4 R² Score (Coeficiente de Determinação)
```
R² = 1 - (SS_residual / SS_total)

Onde:
SS_residual = Σ(y_real - y_predito)²
SS_total = Σ(y_real - y_média)²

Interpretação: proporção de variância explicada [0, 1]
R² = 0.82 → modelo explica 82% da variância
R² = 0.5 → modelo explica 50% da variância
```

---

### 7. Análise de Importância de Features

Para modelos baseados em árvores (Random Forest, Gradient Boosting), calculamos a importância de cada feature.

#### 7.1 Como é Calculada
```
1. Em cada divisão de nó (split), há redução de impureza
2. Importância = Σ(redução de impureza para cada feature)
3. Normaliza-se para somar 100%
```

#### 7.2 Interpretação
```
Feature com importância 40% contribui 40% para as previsões
Features com importância baixa (<5%) podem ser removidas
```

---

## Técnicas de Validação

### Train-Test Split
```
Simples, rápido
Problema: estimativa de desempenho pode variar muito com seed
```

### Recomendação: K-Fold Cross-Validation (Futuro)
```
1. Divide dataset em k=5 folds
2. Treina k modelos
3. Calcula métrica k vezes
4. Reporta média ± desvio padrão
Mais robusto que train-test split único
```

---

## Decisões de Design

1. **Remoção de Outliers**: Outliers removidos do treinamento para evitar viés, mas mantidos para análise
2. **Normalização**: Essencial para SVR e Ridge, beneficia Random Forest
3. **5 Modelos Distintos**: Fornece perspectives diferentes, permite comparação
4. **Métricas Múltiplas**: MAE + RMSE + R² para avaliação completa
5. **Test Set Fixo**: Seed=42 garante reprodutibilidade

---

## Próximos Passos Recomendados

1. Validação cruzada (k-fold)
2. Hyperparameter tuning (GridSearchCV)
3. Engenharia de features (polinômios, interações)
4. Ensemble stacking (combinar modelos)
5. Integração com cloud (AWS SageMaker, GCP Vertex AI)
6. Pipeline automático com CI/CD

