import pandas as pd
import numpy as np


df = pd.read_csv("titanic.csv")

# print(df.shape)
# print(list(df.columns))
# print(df.head(3))

#imprimir solo la columna "Name" utilizando head(3)
# print(df["Name"].head(3))

#combinar condiciones y contar valores
# mujeres_sobrevivientes = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
# print(mujeres_sobrevivientes.shape)

# print(df["Survived"].value_counts())


# precios = pd.Series([25.99, 40.50, 15.75, 60.00])
# print(precios)
# print(type(precios))

"""
EJERCICIO GUIADO

1.crear un DataFrame llamado estudiantes.
2.incluir 3 columnas con la llave: nombre, edad y curso. ( con datos de 4 personas, inventarlo)
3.imprimir dataframe para visualizarlo

"""

# estudiantes = pd.DataFrame({
#  "Nombre": ["angel", "raul", "ernesto", "marcelo"],
#  "Edad":   [12, 15, 13, 16],
#  "Curso":  ["sexto", "septimo", "quinto", "octavo"]
# })

# print(estudiantes)

#eliminar valores filas vacias
# edades = df["Age"].dropna()

# #crear array de numpy con una serie(pandas)
# edades_array = edades.to_numpy()
# print(type(edades_array))

# #formulas utilizadas en numpy para calcular
# print("promedio de edad: ", round(np.mean(edades_array), 1) )
# print("edad maxima: ", np.max(edades_array))
# print("edad minima: ", np.min(edades_array))
# print("desviacion estandar: ", round(np.std(edades_array), 1))

"""
EJERCICIO GUIADO

1.filtrar el DataFrame para quedarse solo con los pasajeros de la columna "Pclass".
2.guardar en una variable nueva e imprimira cuantas filas tienes.
3.despues utilizara el metodo ".value_counts() sobre la columna "Pclass" del DataFrame original.

objetivo: visualizar cuantos pasajeros habia en cada clase
"""


pasajeros = df["Pclass"] == 1
print(pasajeros.shape)
print(df["Pclass"].value_counts())


