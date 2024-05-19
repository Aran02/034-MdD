import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# Wordcloud por palabra
# Cargar el archivo CSV
data = pd.read_csv('HistoricalEsportData.csv')

# Combinar todas las palabras en una sola cadena
text = ' '.join(data['Game'])

# Dividir la cadena en palabras individuales
words = text.split()

# Contar la frecuencia de cada palabra
word_freq = dict(Counter(words))

# Crear el objeto WordCloud con las frecuencias
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud por Palabra')
plt.savefig('wordcloud_por_palabra.png')
plt.show()

# Wordcloud por juego
# Calcular la frecuencia de cada palabra en la columna 'Game'
word_freq = data['Game'].value_counts().to_dict()

# Crear el objeto WordCloud con las frecuencias
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud de Juegos de Esports')
plt.savefig('wordcloud_por_juego.png')
plt.show()

