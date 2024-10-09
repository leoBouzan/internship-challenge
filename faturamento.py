import pandas as pd
import json

# Reading JSON file
with open('faturamento_mensal.json', 'r') as f:
    faturamento_json = json.load(f)

# Converting JSON to DataFrame
faturamento_df = pd.DataFrame(faturamento_json['faturamento'])

# Finding the minimum value
min_value = faturamento_df[faturamento_df['valor'] == faturamento_df['valor'].min()]
print(f"O valor mínimo faturado foi de {min_value['valor'].values[0]:.2f} em {min_value['data'].values[0]}")

# Finding the maximum value
max_value = faturamento_df[faturamento_df['valor'] == faturamento_df['valor'].max()]
print(f"O valor máximo faturado foi de {max_value['valor'].values[0]:.2f} em {max_value['data'].values[0]}")

# Finding the average value
average_value = faturamento_df['valor'].mean()
days_above_average = faturamento_df[faturamento_df['valor'] > average_value]
print(f"O valor médio faturado foi de {average_value:.2f}")
print(f"Os dias em que o valor faturado foi acima do médio foram {days_above_average['data'].values}")
