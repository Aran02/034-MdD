import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Cargar el conjunto de datos
data = pd.read_csv('HistoricalEsportData.csv')

# Definir las clases de ganancias
def categorize_earnings(earnings):
    if earnings < 10000:
        return 'Bajas'
    elif earnings < 1000000:
        return 'Medianas'
    else:
        return 'Altas'

# Aplicar la categorización a la columna de ganancias
data['Earnings_Category'] = data['Earnings'].apply(categorize_earnings)

# Dividir el conjunto de datos en características (X) y etiquetas (y)
X = data[['Players', 'Tournaments']]
y = data['Earnings_Category']

# Dividir el conjunto de datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar las características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Entrenar el clasificador k-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# Predecir las clases en el conjunto de prueba
y_pred = knn.predict(X_test_scaled)

# Graficar los resultados
plt.figure(figsize=(10, 6))

colors = {'Bajas': 'red', 'Medianas': 'green', 'Altas': 'blue'}
plt.scatter(X_test['Players'], X_test['Tournaments'], c=[colors[c] for c in y_pred])
plt.xlabel('Jugadores')
plt.ylabel('Torneos')
plt.title('Clasificacion de Ganancias por KNN')
plt.legend()

plt.savefig('clasification.png')
plt.show()