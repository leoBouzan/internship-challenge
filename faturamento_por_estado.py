import pandas as pd

# Criando uma tabela com os valores de faturamento por estado
data = {
    'Estado': ['SP', 'RJ', 'MG', 'ES', 'Outros'],
    'Valor (R$)': [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
}

fauturamento_por_estado = pd.DataFrame(data)

# Calculando o percentual de cada estado
fauturamento_por_estado['Percentual (%)'] = round(fauturamento_por_estado['Valor (R$)'] / fauturamento_por_estado['Valor (R$)'].sum() * 100, 2)

print(fauturamento_por_estado)
