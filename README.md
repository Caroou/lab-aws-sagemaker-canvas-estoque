# 📊 Previsão de Estoque Inteligente na AWS com [SageMaker Canvas](https://aws.amazon.com/pt/sagemaker/canvas/)

Desafio de projeto "Previsão de Estoque Inteligente na AWS com SageMaker Canvas. Neste Lab DIO, você aprenderá a usar o SageMaker Canvas para criar previsões de estoque baseadas em Machine Learning (ML).

## 🎯 Objetivos Deste Desafio de Projeto (Lab)

![image](https://github.com/digitalinnovationone/lab-aws-sagemaker-canvas-estoque/assets/730492/72f5c21f-5562-491e-aa42-2885a3184650)

## 🚀 Meu Passo a Passo

### 1. Criação e upload do Dataset

-   Com a ajuda de uma Inteligência Artificial Generativa (Gemini), criei um código em Python para gerar um arquivo CSV contendo dados simulados de estoque de uma loja de eletrônicos. Ela possui os seguintes dados (exemplo):

| ID_Produto  | Data  | Quantidade_Vendida  | Promocao  |
|:------------|:------|:--------------------|:----------|
| `LT-001`    | `2024-01-01` | `4`          | `0`       |
| `SM-002`    | `2024-01-01` | `24`         | `1`       |
| `FO-003`    | `2024-01-01` | `15`         | `0`       |
| `SW-004`    | `2024-01-01` | `9`          | `0`       |
| `CD-005`    | `2024-01-01` | `5`          | `0`       |

- Legenda: `LT-001 - Laptop Gamer`, `SM-002 - Smartphone`, `FO-003 - Fone de Ouvido`, `SW-004 - Smartwatch`, `CD-005 - Câmera Digital`

-   Em seguida, realizei o upload do arquivo no SageMaker Canvas e selecionei o dataset desejado para o projeto.

### 2. Construir/Treinar

-   Configurei as variáveis de importância e defini a variável alvo como a `Quantidade_Vendida`.
-   Iniciei o processo de treinamento do modelo pelo SageMaker Canvas.

![construcao](https://i.imgur.com/jNviglD.png)

### 3. Analisar

-   Após o treinamento, examinei as métricas de desempenho e as variáveis com maior influência sobre a `Quantidade_Vendida`.

![analise](https://i.imgur.com/oazg8tP.png)

### 4. Prever

-   Por fim, foi possível gerar a previsão da quantidade de venda para cada um dos itens. O resultado apresentou diferentes cenários de probabilidade de venda durante o período de 1 dia:
-   **P90**: Uma visão otimista de venda (90% de chance de as vendas serem iguais ou maiores que este valor).

-   **P50**: Uma média (valor mediano esperado de vendas).

-   **P10**: Uma visão pessimista de venda (10% de chance de as vendas serem iguais ou menores que este valor).

## 💻 LT-001 - Laptop

![previsao 1](https://i.imgur.com/2AvXsxK.png)

## 📱 SM-002 - Smartphone
![previsao 2](https://i.imgur.com/t3CVQQr.png)

## 🎧 FO-003 - Fone de Ouvido

![previsao 3](https://i.imgur.com/TZh32iP.png)

## ⌚ SW-004 - Smartwatch

![previsao 4](https://i.imgur.com/eT7AXu6.png)

## 📸 CD-005 - Câmera Digital

![previsao 5](https://i.imgur.com/MVl2eB0.png)
