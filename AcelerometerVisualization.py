# bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# importar data
data = pd.read_csv("C:/Users/USUARIO/Downloads/SensorData.csv")

# Convertir indices de columnas a tipos de datos numéricos
data['x'] = pd.to_numeric(data['x'], errors='coerce')
data['y'] = pd.to_numeric(data['y'], errors='coerce')
data['z'] = pd.to_numeric(data['z'], errors='coerce')

# division de datos
x_col = data.loc[:, 'x']
y_col = data.loc[:, 'y']
z_col = data.loc[:, 'z']

# calculos estadisticos

# media
x_media = x_col.mean()
y_media = y_col.mean()
z_media = z_col.mean()

# mediana
x_mediana = x_col.median()
y_mediana = y_col.median()
z_mediana = z_col.median()

# moda
x_moda = x_col.mode()[0] if not x_col.empty else None
y_moda = y_col.mode()[0] if not y_col.empty else None
z_moda = z_col.mode()[0] if not z_col.empty else None

# Calcular la varianza de cada columna
x_varianza = data['x'].var()
y_varianza = data['y'].var()
z_varianza = data['z'].var()

# Calcular el valor máximo de cada columna
x_max = data['x'].max()
y_max = data['y'].max()
z_max = data['z'].max()

# Calcular el valor mínimo de cada columna
x_min = data['x'].min()
y_min = data['y'].min()
z_min = data['z'].min()
# datos por terminal
print("Media del eje 'x':", x_media)
print("Media del eje 'y':", y_media)
print("Media del eje 'z':", z_media)
print('\n')
print("Mediana del eje 'x':", x_mediana)
print("Mediana del eje 'y':", y_mediana)
print("Mediana del eje 'z':", z_mediana)
print('\n')
print("Moda del eje 'x':", x_moda)
print("Moda del eje 'y':", y_moda)
print("Moda del eje 'z':", z_moda)
print('\n')
print("Varianza del eje 'x':", x_varianza)
print("Varianza del eje 'y':", y_varianza)
print("Varianza del eje 'z':", z_varianza)
print('\n')
print("Valor máximo del eje 'x':", x_max)
print("Valor máximo del eje 'y':", y_max)
print("Valor máximo del eje 'z':", z_max)
print('\n')
print("Valor mínimo del eje 'x':", x_min)
print("Valor mínimo del eje 'y':", y_min)
print("Valor mínimo del eje 'z':", z_min)

# visualizacion de datos
fig, axs = plt.subplots(2, 3, figsize=(15, 8))

# Gráfico de Media
axs[0, 0].plot(['x', 'y', 'z'], [x_media, y_media, z_media], marker='o')
axs[0, 0].set_title("Media")
axs[0, 0].set_ylabel('Valor')

# Gráfico de Mediana
axs[0, 1].plot(['x', 'y', 'z'], [x_mediana, y_mediana, z_mediana], marker='o')
axs[0, 1].set_title("Mediana")

# Gráfico de Moda
axs[0, 2].plot(['x', 'y', 'z'], [x_moda, y_moda, z_moda], marker='o')
axs[0, 2].set_title("Moda")

# Gráfico de Varianza
axs[1, 0].plot(['x', 'y', 'z'], [x_varianza, y_varianza, z_varianza], marker='o')
axs[1, 0].set_title("Varianza")
axs[1, 0].set_ylabel('Valor')

# Gráfico de Máximo
axs[1, 1].plot(['x', 'y', 'z'], [x_max, y_max, z_max], marker='o')
axs[1, 1].set_title("Máximo")

# Gráfico de Mínimo
axs[1, 2].plot(['x', 'y', 'z'], [x_min, y_min, z_min], marker='o')
axs[1, 2].set_title("Mínimo")

plt.tight_layout()
plt.show()
