# Metodologia - Entrega 1

Este documento resume a abordagem usada no notebook principal da Entrega 1.

## 1. Objetivo

Prever o rendimento de safra a partir das variaveis climaticas e do tipo de cultura, alem de explorar perfis de produtividade por meio de tecnicas nao supervisionadas.

## 2. Base de dados

Arquivo utilizado:

- `crop_yield.csv`

Variaveis consideradas:

- `Crop`
- `Precipitation (mm day-1)`
- `Specific Humidity at 2 Meters (g/kg)`
- `Relative Humidity at 2 Meters (%)`
- `Temperature at 2 Meters (C)`
- `Yield`

## 3. Analise exploratoria

A etapa exploratoria foi organizada para:

- verificar qualidade da base;
- identificar tipos de dados, ausencias e duplicidades;
- visualizar a distribuicao do rendimento por cultura;
- avaliar correlacoes entre variaveis numericas;
- observar padroes visuais entre clima e rendimento.

## 4. Outliers

Os outliers foram analisados com IQR em dois niveis:

1. `Global`
   Para identificar pontos discrepantes olhando a base completa.
2. `Por cultura`
   Para evitar interpretar como anomalia aquilo que e apenas diferenca estrutural entre culturas.

A decisao metodologica foi **nao remover linhas automaticamente do treino apenas pelo valor bruto de `Yield`**, porque a escala de rendimento varia bastante entre culturas.

## 5. Clusterizacao

Para a exploracao nao supervisionada, foi usado `K-Means` com padronizacao previa das variaveis numericas.

Critérios observados:

- inercia;
- silhouette score;
- interpretabilidade dos grupos.

O objetivo da clusterizacao foi identificar **perfis de produtividade**, e nao alimentar diretamente a etapa supervisionada.

## 6. Modelagem supervisionada

Foram comparados cinco algoritmos de regressao:

1. `Linear Regression`
2. `Ridge Regression`
3. `Random Forest Regressor`
4. `Gradient Boosting Regressor`
5. `SVR`

## 7. Boas praticas aplicadas

- uso da variavel `Crop` na modelagem;
- `Pipeline` para evitar vazamento de dados;
- `OneHotEncoder` para a variavel categorica;
- separacao treino/teste com `stratify` por cultura;
- validacao cruzada no conjunto de treino.

## 8. Metricas

As metricas usadas para comparar os modelos foram:

- `R2`
- `MAE`
- `RMSE`

## 9. Fonte principal

O detalhamento completo da metodologia, com codigo, tabelas, graficos e interpretacoes, esta em:

- `RichardSchmitz_rm567951_pbl_fase5.ipynb`
