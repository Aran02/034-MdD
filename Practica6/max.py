import pandas as pd

# Cargar el archivo CSV en un DataFrame
historical_data = pd.read_csv('HistoricalEsportData.csv')

# Encontrar el valor máximo de la columna 'Earnings'
max_earnings = historical_data['Earnings'].max()

print("El máximo de los ingresos es:", max_earnings)