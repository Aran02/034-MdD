import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cargar el archivo CSV de datos históricos de esports
df = pd.read_csv("HistoricalEsportData.csv")

# Convertir la columna Date a formato de fecha
df['Date'] = pd.to_datetime(df['Date'])

# Gráfico de dispersión
plt.figure()
plt.scatter(df['Players'], df['Earnings'], alpha=0.5)
plt.xlabel('Cantidad de Jugadores')
plt.ylabel('Ganancias')
plt.title('Gráfico de dispersión de Cantidad de Jugadores vs Ganancias')
x = df['Players']
y = df['Earnings']
coefficients = np.polyfit(x, y, 1)
polynomial = np.poly1d(coefficients)
plt.plot(x, polynomial(x), color='red', label='Línea de tendencia')

plt.legend()
plt.grid(True)
plt.savefig('correlation.png')  
plt.show()

# Seleccionar solo columnas numéricas para calcular la matriz de correlación
numeric_cols = df.select_dtypes(include=['int64']).columns
correlation_matrix = df[numeric_cols].corr()
plt.figure()

# Mapa de calor de la matriz de correlación
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de correlación de datos históricos de esports')
plt.savefig('heatmap.png')  
plt.show()
print(correlation_matrix)

# Gráfico de dispersión con regresión lineal
plt.scatter(df['Players'], df['Earnings'], alpha=0.5)
sns.regplot(x='Players', y='Earnings', data=df, scatter=False, color='red', line_kws={"color":"red"})
plt.xlabel('Cantidad de Jugadores')
plt.ylabel('Ganancias')
plt.title('Regresión lineal de Cantidad de Jugadores | Ganancias')
plt.savefig('scatterplot.png') 
plt.show()
