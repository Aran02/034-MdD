import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

df = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\Aran\UANL\S7\MINERIA DE DATOS\PRACTICA 3\csv\HistoricalEsportData.csv")

# Convertir la columna 'Date' a tipo datetime
df['Date'] = pd.to_datetime(df['Date'])

# Gráfico 1: Gráfico de barras de ganancias por juego
earnings_per_game = df.groupby('Game')['Earnings'].sum().sort_values(ascending=False)[:10]
earnings_per_game.plot(kind='bar', figsize=(10, 6))
plt.title('Ganancias por juego (Top 10)')
plt.xlabel('Juego')
plt.ylabel('Ganancias ($)')
plt.xticks(rotation=45)
plt.savefig("C:/Users/DELL/OneDrive/Desktop/Aran/UANL/S7/MINERIA DE DATOS/PRACTICA 3/img/Ganancias_por_juego.png")
plt.show()


# Gráfico 2: Gráfico de líneas de ganancias a lo largo del tiempo
earnings_over_time = df.groupby('Date')['Earnings'].sum()
earnings_over_time.plot(figsize=(10, 6))
plt.title('Ganancias a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Ganancias ($)')
plt.savefig("C:/Users/DELL/OneDrive/Desktop/Aran/UANL/S7/MINERIA DE DATOS/PRACTICA 3/img/Ganancias_a_lo_largo_del_tiempo.png")
plt.show()


# Gráfico 3: Gráfico de barras de cantidad de torneos por juego
tournament_count_per_game = df.groupby('Game')['Tournaments'].sum().sort_values(ascending=False)[:10]
tournament_count_per_game.plot(kind='bar', figsize=(10, 6), color='green')
plt.title('Cantidad de Torneos por Juego (Top 10)')
plt.xlabel('Juego')
plt.ylabel('Cantidad de Torneos')
plt.xticks(rotation=45)
plt.savefig("C:/Users/DELL/OneDrive/Desktop/Aran/UANL/S7/MINERIA DE DATOS/PRACTICA 3/img/Cantidad_de_torneos_por_juego.png")
plt.show()