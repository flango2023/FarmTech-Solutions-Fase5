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

## Sobre a entrega

Esta fase 5 possui duas partes:

1. **Entrega 1 - Machine Learning**
   Analise exploratoria, identificacao de outliers, clusterizacao e comparacao de cinco modelos de regressao para previsao de rendimento de safra.
2. **Entrega 2 - AWS Cloud Computing**
   Comparacao de custos na AWS e justificativa de escolha da regiao para hospedagem da API e do modelo.


## Principal

O material principal da Entrega 1 esta no notebook:

- `RichardSchmitz_rm567951_pbl_fase5.ipynb`

O notebook já está com:

-> celulas executadas;
-> comentarios no codigo;
-> secoes em markdown organizando o raciocinio;
-> graficos para EDA, outliers, clusterizacao e comparacao de modelos;
-> conclusoes e limitacoes ao final.

## Entrega 1

O Notebook segue o fluxo de acordo com o que foi pedido: 

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

## Principais decisoes metodologicas

- A variavel `Crop` foi mantida na modelagem, porque o tipo de cultura faz parte do problema e influencia fortemente o rendimento.
- O pre-processamento foi encapsulado em `Pipeline`, evitando vazamento de dados.
- A divisao entre treino e teste foi feita com `stratify` por cultura.
- A analise de outliers foi comparada de forma global e por cultura, para nao tratar diferencas estruturais entre culturas como se fossem erros.

## Estrutura do repositorio

- `RichardSchmitz_rm567951_pbl_fase5.ipynb` - notebook principal da Entrega 1
- `crop_yield.csv` - base de dados usada na analise
- `requirements.txt` - dependencias Python
- `METODOLOGIA.md` - documentacao complementar
- `EXECUTE_AQUI.md` - observacoes auxiliares

## Como executar

1. Instale as dependencias:

```bash
pip install -r requirements.txt
```

2. Abra o notebook:

```bash
jupyter notebook RichardSchmitz_rm567951_pbl_fase5.ipynb
```

ou

```bash
jupyter lab RichardSchmitz_rm567951_pbl_fase5.ipynb
```


## Video
 

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


### Comparação de custo

De acordo com os valores fornecidos na Medição, conclui-se que:

- `N. Virginia` é a opção mais barata;
- `São Paulo` é de `1.75 USD` por mes acima de `N. Virginia`;
- isso representa aproximadamente `57%` a mais em relacão ao valor de `N. Virginia`.

### Região AWS recomendada para o projeto

Mesmo com custo maior, a região recomendada para este cenario é **South America (São Paulo)**.

Justificativa:

- A proposta do enunciado deixa bem claro que existem **restricoes legais para armazenamento no exterior**;
- manter a infraestrutura no Brasil reduz risco de não conformidade regulatória;
- a proximidade geografica pode ajudar em latencia e acesso mais rápido aos dados dos sensores;
- para uma API que recebe dados agricolas e executa o modelo de ML, conformidade e disponibilidade local tendem a pesar mais do que a menor economia mensal.

## Conclusão

Se o criterio for apenas **menor preço**, a melhor escolha e `US East (N. Virginia)`.

Se o critério considerar **restrição legal de armazenamento e acesso rápido aos dados dos sensores**, a escolha mais adequada é `South America (Sao Paulo)`, mesmo com custo mensal superior.


