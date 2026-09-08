import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")

# print(df.shape)

# print(df.isnull().sum())

# # eliminamos columna "Cabin" porque tiene alrededor de 77% casos nulos
# df = df.drop(columns=["Cabin"])

# #calcular la media de la columna "Age"
# edad_media = df["Age"].median()
# #rellenar cada espacio vacio de la columna "Age"
# df["Age"] = df["Age"].fillna(edad_media)

# #eliminar filas vacias dentro de la columna "Embarked"
# df = df.dropna(subset=["Embarked"])

# print(df.shape)
# #imprime un total de todas las columnas vacias, si no hay vacias debe dar 0
# print(df.isnull().sum().sum())

# """
# EJERCICIO GUIADO

# 1.imprimir la cantidad de columna que tenemos
# 2.confirmar que la columna "Age" ya no tiene nulos
# """

# print(list(df.columns))

# print(df["Age"].isnull().sum())

# #crear columnas nuevas atravez "feacture engineering"
# df["FamiliaTotal"] = df["SibSp"] + df["Parch"] + 1
# print(df[["SibSp", "Parch", "FamiliaTotal"]].head(3))


# #crear columnas para evaluar valores buleanos (true/false)
# df["EsMenorDeEdad"] = df["Age"] < 18
# print(df["EsMenorDeEdad"].value_counts())

# #identificar tipos de datos y ordenarlos
# print(df.dtypes)

# #cambiar tipos de datos de una columna
# df["Survived"] = df["Survived"].astype(bool)
# print(df["Survived"].dtypes)
# print(df["Survived"].head(3))


# #ordenar el dataset de mayor a menor

# df_por_edad = df.sort_values("Age", ascending=False)
# print(df_por_edad[["Name", "Age"]].head(3))

# #agrupar el dataset

promedio_edad_por_clase = df.groupby("Pclass")["Age"].mean()
print(promedio_edad_por_clase)

promedio_edad_por_clase = df.groupby("Pclass")["Survived"].mean()
print(promedio_edad_por_clase.round(3))

df.to_csv("titanic_limpio", index=False)