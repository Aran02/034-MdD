import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cargar el conjunto de datos desde el archivo CSV
data = pd.read_csv("HistoricalEsportData.csv")

# Sumar las ganancias por año
earnings_by_year = data.groupby(data['Date'].str[-4:])['Earnings'].sum()

# Convertir los años y las ganancias en arrays NumPy
x = np.array([int(year) for year in earnings_by_year.index])
y = earnings_by_year.values

# Definir la función para calcular la predicción
def fx(x1, coef):
    fx = 0
    n = len(coef) - 1
    for p in coef:
        fx = fx + p*x1**n
        n = n - 1
    return fx

# Año para el cual se desea hacer la predicción
anno = 2021

# Iterar sobre diferentes grados de polinomio
for i in range(1, 10):
    # Ajustar un polinomio de grado i a los datos
    coef = np.polyfit(x, y, i)
    
    # Calcular la predicción para el año 2024
    p = np.polyval(coef, anno)
    
    # Imprimir la predicción
    print(f"Para grado {i}, la predicción de ganancias para el año {anno} es: {p:.2f}")
    
    # Calcular la función polinómica ajustada
    x1 = np.linspace(min(x), anno + 1, 1000)
    y1 = fx(x1, coef)
    
    # Graficar los datos y la función polinómica ajustada
    plt.figure(figsize=[10, 6])
    plt.title("Ganancias anuales")
    plt.scatter(x, y, s=50, c='blue', label='Datos Originales')
    plt.plot(x1, y1, "--", linewidth=2, color='orange', label='Ajuste Polinómico')
    plt.scatter(anno, p, s=100, c='red', label='Predicción 2024')
    plt.xlabel("Año")
    plt.ylabel("Ganancias")
    plt.legend()
    plt.grid(True)
    plt.savefig(f'forecasting_grado_{i}.png')
    plt.show()

# Grado del polinomio vs MSE
# Un MSE más bajo indica un mejor ajuste, ya que significa que las predicciones del modelo se acercan más a los valores reales.
# Por otro lado, un MSE más alto indica que las predicciones del modelo están más alejadas de los valores reales, lo que indica un ajuste deficiente.
anno = 2021  # Cambia el año al que quieres predecir
grado = np.arange(0, 30 + 1, 1)  # Rango de grados de polinomio
MSE_array = np.array([])

for i in grado:
    coef = np.polyfit(x, y, i)
    p = np.polyval(coef, anno)
    
    # Calcular el error cuadrático medio (MSE)
    y_pred_vec = np.polyval(coef, x)
    MSE = np.mean((y - y_pred_vec)**2)
    MSE_array = np.append(MSE_array, MSE)
    
    print(f"Para grado {i}, el MSE es: {MSE}")

# Graficar el grado del polinomio vs MSE
plt.figure(figsize=[10, 6])
plt.title("Grado del polinomio vs MSE")
plt.plot(grado, MSE_array, "--", linewidth=3, color='red')
plt.xlabel("Grado del polinomio")
plt.ylabel("MSE")
plt.grid(True)
plt.savefig('grado_vs_MSE.png')
plt.show()
