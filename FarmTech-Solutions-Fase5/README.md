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

Esta fase possui duas partes:

1. **Entrega 1 - Machine Learning**
   Analise exploratoria, identificacao de outliers, clusterizacao e comparacao de cinco modelos de regressao para previsao de rendimento de safra.
2. **Entrega 2 - Cloud Computing**
   Comparacao de custos na AWS e justificativa de escolha da regiao para hospedagem da API e do modelo.


## Artefato principal

O material principal da Entrega 1 esta no notebook:

- `RichardSchmitz_rm567951_pbl_fase5.ipynb`

O notebook ja esta com:

- celulas executadas;
- comentarios no codigo;
- secoes em markdown organizando o raciocinio;
- graficos para EDA, outliers, clusterizacao e comparacao de modelos;
- conclusoes e limitacoes ao final.

## O que foi feito na Entrega 1

O notebook segue o fluxo pedido no enunciado:

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

### Execucao no Google Colab

Se abrir a versao `FarmTech_Solutions_Fase5_Colab.ipynb` no Colab, o notebook agora possui:

- uma celula para montar o Google Drive;
- busca automatica por `crop_yield.csv` em `/content/drive/MyDrive/`;
- fallback para upload manual, se o arquivo nao for encontrado.

Se quiser evitar upload manual, basta deixar o CSV em um destes caminhos:

- `/content/drive/MyDrive/crop_yield.csv`
- `/content/drive/MyDrive/FarmTech-Solutions-Fase5/crop_yield.csv`

## Video

O link do video demonstrativo sera adicionado nesta secao:

- `YouTube (nao listado)`: pendente

## Entrega 2 - AWS

Com base no PDF exportado do AWS Pricing Calculator presente no repositorio (`medicao_aws.pdf`), foi realizada uma comparacao entre as regioes:

- `US East (N. Virginia)`
- `South America (Sao Paulo)`

### Valores identificados no PDF

Os valores extraidos do relatorio foram:

| Regiao | Custo mensal | Custo upfront |
|---|---:|---:|
| US East (N. Virginia) | `3.07 USD` | `0.00 USD` |
| South America (Sao Paulo) | `4.82 USD` | `0.00 USD` |

Resumo do relatorio exportado:

- custo mensal total mostrado no PDF: `7.89 USD`
- custo total em 12 meses mostrado no PDF: `94.68 USD`

### Configuracao identificada no relatorio

No PDF exportado, a configuracao registrada pela calculadora aparece como:

- `Amazon EC2`
- `Linux`
- `2 instancias`
- `EC2 instance: t4g.nano`
- `Pricing strategy: Compute Savings Plans 3yr No Upfront`

### Comparacao de custo

Pelos valores medidos no relatorio:

- `N. Virginia` foi a opcao mais barata;
- `Sao Paulo` ficou `1.75 USD` por mes acima de `N. Virginia`;
- isso representa aproximadamente `57%` a mais em relacao ao valor de `N. Virginia`.

### Escolha recomendada para o projeto

Mesmo com custo maior, a regiao recomendada para este cenario e **Sao Paulo**.

Justificativa:

- o enunciado informa que existem **restricoes legais para armazenamento no exterior**;
- manter a infraestrutura no Brasil reduz risco de nao conformidade regulatoria;
- a proximidade geografica pode ajudar em latencia e acesso mais rapido aos dados dos sensores;
- para uma API que recebe dados agricolas e executa o modelo de ML, conformidade e disponibilidade local tendem a pesar mais do que a menor economia mensal.

### Conclusao da Entrega 2

Se o criterio for apenas **menor preco**, a melhor escolha e `US East (N. Virginia)`.

Se o criterio considerar **restricao legal de armazenamento e acesso rapido aos dados dos sensores**, a escolha mais adequada e `South America (Sao Paulo)`, mesmo com custo mensal superior.

### Observacao importante

O PDF anexado foi usado como base desta secao porque ele representa a medicao realizada no AWS Pricing Calculator. Ainda assim, o relatorio exportado mostra uma configuracao com `2 instancias t4g.nano` e `Savings Plan`, enquanto o enunciado pede comparacao com `On-Demand 100%`, `2 CPUs`, `1 GiB` e `50 GB` de armazenamento. Por isso, esta secao documenta fielmente os valores do PDF, mas a revisao final da calculadora pode ser interessante caso voce queira aderencia literal maxima ao enunciado.

## Observacao final

O `README` foi mantido intencionalmente introdutorio. O detalhamento completo da solucao, com analises, metricas, graficos e conclusoes, esta dentro do notebook principal.
