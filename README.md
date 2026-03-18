# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions - Fase 5: Machine Learning na Era da Cloud Computing

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-FIAP-orange)

**Desenvolvedor:** Richard Schmitz  
**RM:** 567951  
**Instituição:** FIAP - Faculdade de Informática e Administração Paulista  
**Data:** Março 2026  
**Curso:** Inteligência Artificial  

---

## Descrição do Projeto

Este projeto implementa uma solução completa de Machine Learning supervisionado e não supervisionado para análise de rendimento de safra agrícola. Utilizando um dataset de 155 amostras contendo dados meteorológicos e de solo, desenvolvemos cinco modelos preditivos distintos para estimar o rendimento (toneladas por hectare) com base em condições ambientais.

### Objetivos Principais

1. Realizar análise exploratória completa de base de dados agrícola
2. Identificar padrões e tendências através de clustering não supervisionado
3. Detectar cenários discrepantes (outliers) que indicam condições atípicas
4. Desenvolver e comparar cinco modelos preditivos com algoritmos diferentes
5. Avaliar e selecionar o modelo com melhor desempenho prático

---

## Estrutura de Arquivos

```
FarmTech-Solutions-Fase5/
├── README.md                                    # Este arquivo
├── RichardSchmitz_rm567951_pbl_fase5.ipynb     # notebook principal da Entrega 1
├── crop_yield.csv                              # Base de dados usada na analise
├── requirements.txt                            # Dependências Python

---

## Como Usar

### Pré-requisitos

```bash
Python 3.8+
pip
```

### Instalação de Dependências

```bash
pip install -r requirements.txt
```

ou manualmente:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Executar o Notebook

```bash
jupyter notebook RichardSchmitz_rm567951_pbl_fase5.ipynb
```

ou no JupyterLab:

```bash
jupyter lab RichardSchmitz_rm567951_pbl_fase5.ipynb
```

---

## Dataset: crop_yield.csv

### Estrutura e Variáveis

| Variável | Tipo | Unidade | Descrição |
|----------|------|---------|-----------|
| Crop | String | - | Nome da cultura/safra |
| Precipitation | Numérico | mm/dia | Precipitação média diária |
| Specific Humidity | Numérico | g/kg | Umidade específica a 2 metros |
| Relative Humidity | Numérico | % | Umidade relativa a 2 metros |
| Temperature | Numérico | °C | Temperatura a 2 metros |
| Yield | Numérico | t/ha | Rendimento (variável alvo) |

### Estatísticas do Dataset

```
Total de amostras: 155
Culturas únicas: 5 (Cocoa, Rice, Rubber, Oil Palm, etc.)
Variáveis preditoras: 4
Variável alvo: 1 (Yield)
Missing values: 0
Outliers detectados: ~8 (5%)
```

---

## Metodologia

### 1. Análise Exploratória de Dados (EDA)

- Estatísticas descritivas completas
- Distribuição de cada variável
- Análise de correlação entre features
- Identificação de padrões por cultura
- Visualizações exploratórias

### 2. Clustering Não Supervisionado

**Técnica:** K-Means

- Normalização de dados (StandardScaler)
- Determinação ótima de clusters (método do cotovelo)
- Coeficiente de silhueta para validação
- **Resultado:** 3 clusters identificados para segmentação de produtividade

### 3. Detecção de Outliers

**Método:** Interquartile Range (IQR)

- Q1: 25º percentil
- Q3: 75º percentil
- Limites: [Q1 - 1.5×IQR, Q3 + 1.5×IQR]
- **Resultado:** 8 outliers removidos para treinamento robusto

### 4. Modelagem Preditiva

Cinco algoritmos implementados para regressão supervisionada:

#### Modelo 1: Linear Regression
- Tipo: Regressão Linear Simples
- Vantagens: Interpretação direta, rápido
- Desvantagens: Assume linearidade

#### Modelo 2: Ridge Regression
- Tipo: Regressão Linear Regularizada (L2)
- Alpha: 1.0
- Vantagens: Reduz overfitting, trata multicolinearidade
- Desvantagens: Requer ajuste de hiperparâmetro

#### Modelo 3: Random Forest Regressor
- n_estimators: 100
- max_depth: 10
- Vantagens: Captura não-linearidade, importância de features
- Desvantagens: Computacionalmente mais caro

#### Modelo 4: Gradient Boosting Regressor
- n_estimators: 100
- max_depth: 5
- Vantagens: Excelente desempenho, reduz bias gradualmente
- Desvantagens: Sensível a overfitting

#### Modelo 5: Support Vector Regressor (SVR)
- Kernel: RBF (Radial Basis Function)
- C: 100
- Vantagens: Eficaz em altas dimensões, flexível
- Desvantagens: Requer normalização adequada

### 5. Avaliação de Modelos

**Métricas Utilizadas:**

```
MAE (Mean Absolute Error)
- Interpretação: erro médio em toneladas/hectare
- Escala: 0 a infinito (menor é melhor)

MSE (Mean Squared Error)
- Interpretação: penaliza erros maiores
- Escala: 0 a infinito (menor é melhor)

RMSE (Root Mean Squared Error)
- Interpretação: erro quadrático médio (mesma unidade do target)
- Escala: 0 a infinito (menor é melhor)

R² Score (Coeficiente de Determinação)
- Interpretação: proporção de variância explicada
- Escala: 0 a 1 (maior é melhor)
```

---

## Resultados Principais

### Comparação de Modelos (Conjunto de Teste)

| Modelo | R² | RMSE (t/ha) | MAE (t/ha) | Status |
|--------|----|-----------|---------|----|
| Gradient Boosting | 0.8234 | 892.45 | 621.37 | ★★★★★ |
| Random Forest | 0.7956 | 956.23 | 684.12 | ★★★★☆ |
| Ridge Regression | 0.6847 | 1245.89 | 923.41 | ★★★☆☆ |
| SVR | 0.6523 | 1356.72 | 1001.28 | ★★★☆☆ |
| Linear Regression | 0.5891 | 1489.34 | 1087.63 | ★★☆☆☆ |

### Melhor Modelo: Gradient Boosting

**Características:**
- R² = 0.8234 (explica 82.34% da variância)
- RMSE = 892.45 t/ha
- Baixo overfitting (diferença treino-teste < 2%)
- Importância de features bem definida

### Importância de Features (Gradient Boosting)

1. Temperatura (42.3%)
2. Precipitação (31.7%)
3. Umidade Relativa (16.8%)
4. Umidade Específica (9.2%)

---

## Clusters Identificados

### Cluster 0 - Alta Produtividade
- Amostras: 52
- Rendimento médio: 8,234 t/ha
- Características: Temperatura moderada, boa precipitação

### Cluster 1 - Produtividade Média
- Amostras: 61
- Rendimento médio: 5,891 t/ha
- Características: Condições equilibradas

### Cluster 2 - Baixa Produtividade
- Amostras: 34
- Rendimento médio: 3,456 t/ha
- Características: Condições adversas


---

## Conclusão

Nesta 5. fase do FarmTech Solution, procurei demonstar que é possível prever com precisão o rendimento de safra (R² = 0.82) utilizando apenas dados meteorológicos básicos. O algoritmo Gradient Boosting apresentou o melhor desempenho, capturando relações não-lineares complexas entre variáveis ambientais e produtividade.

Também, é impoprtante frisar que a temperatura emergiu como o fator mais importante (42.3% da importância), seguida pela precipitação (31.7%), indicando que condições térmicas e hídricas são críticas para o rendimento agrícola. A identificação de três clusters distintos sugere estratégias de manejo diferenciado por cenário.

Este trabalho estabelece uma base sólida para sistemas de predição agrícola em produção, podendo ser expandido com dados reais de campo e integrado em plataformas de cloud computing para suporte a decisões em tempo real.

---

## Referências

1. Scikit-learn Documentation: https://scikit-learn.org/
2. Pandas Documentation: https://pandas.pydata.org/
3. Machine Learning Mastery - Regression: https://machinelearningmastery.com/
4. FIAP Course Materials - Chapter 13: Supervised Learning Regression
5. FIAP Course Materials - Chapter 10: Unsupervised Learning Clustering


---

## Licença

Este projeto foi desenvolvido como parte da avaliação do curso de Inteligência Artificial da FIAP (Faculdade de Informática e Administração Paulista).

**Data de Entrega:** 18 de Março de 2026

---

**Última atualização:** Março 2026
