import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Cargar el archivo CSV
df = pd.read_csv("HistoricalEsportData.csv")

# Definir el número de los principales juegos a considerar
top_games_count = 5  

# Agrupar los datos por 'Game' y calcular las ganancias totales para cada juego
game_total_earnings = df.groupby('Game')['Earnings'].sum().nlargest(top_games_count)

# Filtrar los datos para los principales juegos
data_top_games = df[df['Game'].isin(game_total_earnings.index)]

# Crear un gráfico de caja para mostrar la distribución de las ganancias para los principales juegos
plt.figure(figsize=(10, 10))
sns.boxplot(x='Game', y='Earnings', data=data_top_games)
plt.xlabel('Juego')
plt.ylabel('Ganancias Totales')
plt.title(f'Distribución de Ganancias para los Top {top_games_count} Juegos')
plt.xticks(rotation=45)
plt.grid(True)

# Guardar la gráfica como una imagen
plt.savefig("boxplot_earnings.png")

# Mostrar la gráfica
plt.show()

# Realizar una prueba ANOVA de una vía para determinar si existen diferencias significativas en las ganancias entre los juegos
game_groups = [data_top_games[data_top_games['Game'] == game]['Earnings'] for game in game_total_earnings.index]
data_top_games = data_top_games.dropna()
for game, earnings in zip(game_total_earnings.index, game_groups):
    print(f"Juego: {game}")
    print(earnings)
    print()

f_statistic, p_value = f_oneway(*game_groups)

# Imprimir resultados
print(f'Estadística F del ANOVA de una vía: {f_statistic:.2f}')
print(f'Valor p: {p_value:.4f}')

# Interpretar los resultados
alpha = 0.05  
if p_value < alpha:
    print("Existen diferencias significativas en las ganancias entre los principales juegos.")
    # Realizar la prueba de Tukey
    tukey_results = pairwise_tukeyhsd(data_top_games['Earnings'], data_top_games['Game'])
    print(tukey_results)

else:
    print("No existen diferencias significativas en las ganancias entre los principales juegos.")
