# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FarmTech Solutions Fase 5 - Machine Learning na Era da Cloud Computing

![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-FIAP-orange)

**Desenvolvedor:** Richard Schmitz  
**RM:** 567951  
**Instituição:** FIAP - Faculdade de Informática e Administração Paulista  
**Data:** Março 2026  
**Curso:** Inteligência Artificial  

## Video --->   https://www.youtube.com/watch?v=S6LL8k55jjg

## Descrição do Projeto

Este projeto implementa uma solução completa de Machine Learning supervisionado e não supervisionado para análise de rendimento de safra agrícola. Utilizando um dataset de 157 amostras contendo dados meteorológicos e de solo, desenvolvemos cinco modelos preditivos distintos para estimar o rendimento (toneladas por hectare) com base em condições ambientais.

### Objetivos Principais

1. Realizar análise exploratória completa de base de dados agrícola
2. Identificar padrões e tendências através de clustering não supervisionado
3. Detectar cenários discrepantes (outliers) que indicam condições atípicas
4. Desenvolver e comparar cinco modelos preditivos com algoritmos diferentes
5. Avaliar e selecionar o modelo com melhor desempenho prático

 
## Sobre a entrega

Esta fase 5 contém duas entregas:

1. **Entrega 1 - Machine Learning**
   Analise exploratoria, identificacao de outliers, clusterizacao e comparacao de cinco modelos de regressao para previsao de rendimento de safra.
2. **Entrega 2 - AWS Cloud Computing**
   Comparacao de custos na AWS e justificativa de escolha da regiao para hospedagem da API e do modelo.

## Entrega 1

O Notebook  - `RichardSchmitz_rm567951_pbl_fase5.ipynb` segue o fluxo de acordo com o que foi pedido: 

1. carregamento e auditoria da base `crop_yield.csv`;
2. analise exploratoria das culturas e das variaveis climaticas;
3. identificacao de cenarios discrepantes com IQR;
4. clusterizacao com `K-Means` para explorar perfis de produtividade;
5. treinamento e avaliacao de cinco algoritmos de regressao.

Os cinco modelos comparados foram:

- `Linear Regression`
- `Ridge Regression`
- `Random Forest Regressor`
- `Gradient Boosting Regressor`
- `Support Vector Regressor (SVR)`


## Estrutura do repositorio

```
FarmTech-Solutions-Fase5/
├── README.md                                    # Este arquivo
├── RichardSchmitz_rm567951_pbl_fase5.ipynb     # notebook principal da Entrega 1
├── crop_yield.csv                              # Base de dados usada na analise
├── requirements.txt                            # Dependências Python

---


## Como executar

1. Instale as dependencias:

```bash
pip install -r requirements.txt
```

2. Abra o notebook:

```bash
jupyter notebook - `RichardSchmitz_rm567951_pbl_fase5.ipynb`
```

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
Total de amostras: 156
Culturas únicas: 5 (Cocoa, Rice, Rubber, Oil Palm, etc.)
Variáveis preditoras: 4
Variável alvo: 1 (Yield)
Missing values: 0
Outliers detectados: ~8 (5%)
```



# Entrega 2 - AWS

Com base no AWS Pricing Calculator presente no repositorio (`medicao_aws.pdf`), foi realizada uma comparacao entre as regioes:

- `US East (N. Virginia)`
- `South America (São Paulo)`

### Valores da Medição 

Os valores extraidos do relatório foram:

| Regiao | Custo mensal | Custo upfront |
|---|---:|---:|
| US East (N. Virginia) | `3.07 USD` | `0.00 USD` |
| South America (São Paulo) | `4.82 USD` | `0.00 USD` |

Resumo da medição:

- custo mensal total: `7.89 USD`
- custo total em 12 meses: `94.68 USD`


### Comparação de custos

De acordo com os valores fornecidos na Medição, conclui-se que:

- `N. Virginia` é a opção mais barata;
- `São Paulo` é de `1.75 USD` por mes acima de `N. Virginia`;
- Logo, isso representa aproximadamente `57%` a mais em relacão ao valor de `N. Virginia`.

### AWS Região recomendada para o projeto

Mesmo com custo maior, a região recomendada para este cenario é **South America (São Paulo)**.

Justificativa:

- A proposta do enunciado deixa bem claro que existem **restricoes legais para armazenamento no exterior**;
- manter a infraestrutura no Brasil reduz risco de não conformidade regulatória;
- a proximidade geografica pode ajudar em latencia e acesso mais rápido aos dados dos sensores;
- para uma API que recebe dados agricolas e executa o modelo de ML, conformidade e disponibilidade local tendem a pesar mais do que a menor economia mensal.

## Conclusão

Se o criterio for apenas **menor preço**, a melhor escolha e `US East (N. Virginia)`.

Se o critério considerar **restrição legal de armazenamento e acesso rápido aos dados dos sensores**, a escolha mais adequada é `South America (Sao Paulo)`, mesmo com custo mensal superior.


## Referências

1. Scikit-learn Documentation: https://scikit-learn.org/
2. Pandas Documentation: https://pandas.pydata.org/
3. Machine Learning Mastery - Regression: https://machinelearningmastery.com/
4. FIAP Course Materials - Chapter 13: Supervised Learning Regression
5. FIAP Course Materials - Chapter 10: Unsupervised Learning Clustering


---

## Licença
Este projeto foi deselvovido, em partes, com o auxílio de ferramentas de AI, tais como: Claude | Amazon Q ( Titãn) 
Este projeto foi desenvolvido como parte da avaliação do curso de Inteligência Artificial da FIAP (Faculdade de Informática e Administração Paulista).

**Data de Entrega:** 18 de Março de 2026

---


