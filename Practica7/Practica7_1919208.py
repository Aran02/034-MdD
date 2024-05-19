import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Cargar los datos desde el archivo CSV
data = pd.read_csv("HistoricalEsportData.csv")

# Seleccionar las características relevantes para el clustering
X = data[['Players', 'Tournaments']]

# Escalar los datos para mejorar el rendimiento del clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar el algoritmo KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(X_scaled)
data['Cluster'] = kmeans.labels_

# Colores para los clusters
colors = ['red', 'green', 'blue']

# Visualizar los resultados del clustering
plt.figure(figsize=(10, 6))
for cluster in range(3):
    cluster_data = data[data['Cluster'] == cluster]
    plt.scatter(cluster_data['Players'], cluster_data['Tournaments'], c=colors[cluster], label=f'Cluster {cluster+1}', s=50, alpha=0.5)

# Mostrar los centroides
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, color='black', label='Centroides')
# print("Centroides de cada cluster:")
# for i, centroid in enumerate(centroids):
#     print(f"Cluster {i+1}: Jugadores = {centroid[0]}, Torneos = {centroid[1]}")

# Mostrar y guardar la gráfica
plt.xlabel('Players')
plt.ylabel('Tournaments')
plt.title('Clustering de Jugadores y Torneos')
plt.legend()
plt.grid(True)
plt.savefig('clustering.png')
plt.show()

