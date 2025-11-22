import pandas as pd
import numpy as np
from datetime import timedelta

# 1. Definição dos Produtos
products = {
    'LT-001': 'Laptop Gamer',
    'SM-002': 'Smartphone',
    'FO-003': 'Fone de Ouvido',
    'SW-004': 'Smartwatch',
    'CD-005': 'Câmera Digital'
}

# 2. Geração da Estrutura Base
start_date = pd.to_datetime('2024-01-01')
num_days = 100
dates = [start_date + timedelta(days=i) for i in range(num_days)]

data = []
for date in dates:
    for product_id, product_name in products.items():
        data.append({
            'Data': date,
            'ID_Produto': product_id,
        })

df_simple = pd.DataFrame(data)

# 3. Geração de Dados Simulado
np.random.seed(42) # Para reprodutibilidade

# Simulação de Vendas (Quantidade_Vendida)
sales_ranges_simple = {
    'FO-003': (5, 30),  # Alto volume
    'SM-002': (3, 20),
    'SW-004': (2, 15),
    'CD-005': (1, 10),
    'LT-001': (1, 5)   # Baixo volume
}

def generate_sales_simple(row):
    low, high = sales_ranges_simple[row['ID_Produto']]
    return np.random.randint(low, high + 1)

df_simple['Quantidade_Vendida'] = df_simple.apply(generate_sales_simple, axis=1)

# Simulação de Promoções
# Cerca de 20% dos dias terão promoção (1)
df_simple['Promocao'] = np.random.choice([0, 1], size=len(df_simple), p=[0.8, 0.2])

# Ajuste de vendas baseado em promoção (aumenta as vendas em 20% a 50%)
df_simple['Quantidade_Vendida'] = np.where(
    df_simple['Promocao'] == 1,
    (df_simple['Quantidade_Vendida'] * np.random.uniform(1.2, 1.5)).astype(int),
    df_simple['Quantidade_Vendida']
)

# Limpeza e Organização Final
df_simple = df_simple[['ID_Produto', 'Data', 'Quantidade_Vendida', 'Promocao']]

# Garante que temos pelo menos 500 linhas (5 produtos * 100 dias = 500 linhas)
# Se tivéssemos menos, seria necessário aumentar o num_days.
# O DataFrame já tem 500 linhas.

# Salva para CSV
file_name_simple = 'estoque_simples_analise.csv'
df_simple.to_csv(file_name_simple, index=False)

print(f"Arquivo salvo como {file_name_simple}")
print(df_simple.head())
print(df_simple.info())