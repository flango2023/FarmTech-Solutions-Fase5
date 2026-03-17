# Roteiro de Apresentação - FarmTech Solutions Fase 5

**Apresentador:** Richard Schmitz (RM: 567951)  
**Data:** Março 2026  
**Duração estimada:** 8-10 minutos  

---

## 1. Introdução (1 minuto)

**Objetivo:** Apresentar o projeto e contexto.

**Conteúdo:**
- Saudação e apresentação pessoal
- "Olá, sou Richard Schmitz, estudante de Inteligência Artificial na FIAP. Hoje vou apresentar o projeto FarmTech Solutions - Fase 5, que implementa Machine Learning em produção agrícola."
- Contexto: "Este projeto visa otimizar o rendimento de safras através de análise de dados meteorológicos e de solo, utilizando técnicas de ML supervisionado e não supervisionado."

**Visual:** Mostrar o README.md aberto no Colab ou VS Code.

---

## 2. Visão Geral do Dataset (1.5 minutos)

**Objetivo:** Explicar os dados utilizados.

**Conteúdo:**
- "O dataset contém 156 amostras de diferentes culturas agrícolas."
- "Variáveis: Precipitação, Umidade Específica, Umidade Relativa, Temperatura (preditoras) e Yield (rendimento em t/ha - variável alvo)."
- "Dados reais de condições ambientais que afetam a produtividade."

**Visual:** Executar o script Python e mostrar as primeiras linhas do dataset.

```python
# No Colab
!python FarmTech_Solutions_Fase5_Colab.py
# Mostrar output inicial
```

---

## 3. Análise Exploratória de Dados (EDA) (2 minutos)

**Objetivo:** Demonstrar a exploração inicial dos dados.

**Conteúdo:**
- "Iniciamos com análise exploratória para entender a distribuição e correlações."
- "Verificamos estatísticas descritivas, valores ausentes (nenhum) e correlações entre variáveis."
- "Observamos que temperatura e rendimento têm outliers, indicando condições atípicas."

**Visual:** 
- Mostrar histogramas das variáveis
- Matriz de correlação
- Box plots para outliers

**Dica:** "Como podemos ver, há correlação moderada entre umidade e rendimento."

---

## 4. Clustering Não Supervisionado (1.5 minutos)

**Objetivo:** Explicar a segmentação dos dados.

**Conteúdo:**
- "Aplicamos K-Means clustering para identificar padrões nos dados."
- "Usamos o método do cotovelo para determinar K=3 clusters ótimos."
- "Os clusters revelam diferentes perfis de produtividade agrícola."

**Visual:**
- Gráfico do cotovelo
- Visualização PCA dos clusters
- Estatísticas médias por cluster

**Dica:** "O Cluster 2 mostra maior rendimento médio, associado a condições específicas de umidade."

---

## 5. Detecção de Outliers (1 minuto)

**Objetivo:** Justificar a limpeza de dados.

**Conteúdo:**
- "Detectamos outliers usando o método IQR (Interquartile Range)."
- "Removemos 45 amostras atípicas para melhorar a performance dos modelos."
- "Isso resulta em dados mais robustos para modelagem."

**Visual:** Mostrar contagem de outliers por variável.

---

## 6. Modelos Preditivos (2 minutos)

**Objetivo:** Apresentar os 5 modelos implementados.

**Conteúdo:**
- "Desenvolvemos 5 modelos de regressão: Linear, Ridge, Random Forest, Gradient Boosting e SVR."
- "Avaliamos usando MSE, MAE e R²."
- "O melhor modelo foi Regressão Linear, apesar dos valores de R² negativos indicarem necessidade de mais features ou pré-processamento."

**Visual:**
- Tabela de resultados dos modelos
- Gráfico de comparação de R² (mostrar o PNG salvo)

**Dica:** "Os R² negativos sugerem que os modelos atuais não capturam bem a variabilidade dos dados, indicando oportunidade para melhorias futuras."

---

## 7. Conclusão e Lições Aprendidas (1 minuto)

**Objetivo:** Encerrar a apresentação.

**Conteúdo:**
- "Concluímos a implementação completa de ML para agricultura."
- "Principais aprendizados: Importância da EDA, poder do clustering para insights, e necessidade de dados de qualidade para modelos preditivos."
- "Este projeto demonstra aplicação prática de IA em agronegócio."

**Visual:** Mostrar o repositório no GitHub (sem commit do roteiro).

---

## Dicas Gerais para Apresentação

- **Ritmo:** Falar pausadamente, explicar termos técnicos.
- **Interação:** Pausar para mostrar códigos e outputs.
- **Tempo:** Manter dentro de 10 minutos.
- **Preparação:** Testar execução completa no Colab antes.
- **Backup:** Ter prints dos gráficos caso algo falhe.

---

**Script de Execução no Colab:**

```bash
# Clone o repo
!git clone https://github.com/flango2023/FarmTech-Solutions-Fase5.git
%cd FarmTech-Solutions-Fase5

# Instala dependências
!pip install -r requirements.txt

# Executa análise completa
!python FarmTech_Solutions_Fase5_Colab.py

# Mostra gráfico salvo
from IPython.display import Image
Image('model_comparison.png')
```
