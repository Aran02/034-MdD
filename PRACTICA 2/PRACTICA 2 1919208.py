import pandas as pd 

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Aran\UANL\S7\MINERIA DE DATOS\PRACTICA 2\csv\HistoricalEsportData.csv")

# Mostrar las primeras filas del DataFrame para verificar que se haya cargado correctamente
print(df.head())

# Agrupar por el nombre del juego y calcular estadísticas descriptivas
grouped_stats = df.groupby('Game').agg({
    'Earnings': ['sum', 'mean', 'median', 'min', 'max'],
    'Players': ['sum', 'mean', 'median', 'min', 'max'],
    'Tournaments': ['sum', 'mean', 'median', 'min', 'max']
})

# Mostrar las estadísticas descriptivas agrupadas
print(grouped_stats)

# Guardar el DataFrame con las estadísticas descriptivas en un nuevo archivo CSV
grouped_stats.to_csv("C:/Users/DELL/OneDrive/Desktop/Aran/UANL/S7/MINERIA DE DATOS/PRACTICA 2/csv/GroupedStats.csv")