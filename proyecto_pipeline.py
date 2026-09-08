import pandas as pd

#Cargar	y	diagnosticar

df = pd.read_csv("hollywood.csv")

# print(df.shape)
# print(df.head())

df_filtrado = df[["Movie", "LeadStudio", "Genre", "RottenTomatoes",	"AudienceScore",
"WorldGross", "Budget",	"Year"]]

# print(df_filtrado.shape)

# print(df_filtrado.isnull().sum())

#Limpiar

df_filtrado[["Genre", "LeadStudio"]] = df_filtrado[["Genre", "LeadStudio"]].fillna("Desconocido")
print(df_filtrado[["Genre", "LeadStudio"]].isnull().sum())

promedio_de_RottenT_y_AudienceS = df_filtrado[["RottenTomatoes", "AudienceScore"]].median()
df_filtrado[["RottenTomatoes", "AudienceScore"]] = df_filtrado[["RottenTomatoes", "AudienceScore"]].fillna(promedio_de_RottenT_y_AudienceS)
print(df_filtrado[["RottenTomatoes", "AudienceScore"]].isnull().sum())

df_filtrado = df_filtrado.dropna(subset=["WorldGross", "Budget"])
# df_filtrado = df_filtrado.drop(columns=["WorldGross", "Budget"])


# Crear	columnas nuevas

df_filtrado["Ganancia"] = df_filtrado["WorldGross"] - df_filtrado["Budget"]

df_filtrado["Exitosa"] = df_filtrado["RottenTomatoes"] >= 60
print(df_filtrado["Exitosa"].value_counts())

print(df_filtrado[["WorldGross", "Budget", "Ganancia" ]].head())

# print(df_filtrado.columns)
# print(df_filtrado.shape)
# print(df_filtrado[["WorldGross","Budget"]].isnull().sum())

#Tipos	de	datos	y	ordenar

print(df_filtrado["Exitosa"].dtypes)

Ganancia_de_mayor_a_menor = df_filtrado.sort_values("Ganancia", ascending= False)
print(Ganancia_de_mayor_a_menor.head(3))


#Agrupar	y	analizar

promedio_RottenTomatoes_con_Genre = df_filtrado.groupby("Genre")["RottenTomatoes"].mean().round(1)
print(promedio_RottenTomatoes_con_Genre.head())

promedio_Ganacia_con_LeadStudio = df_filtrado.groupby("LeadStudio")["Ganancia"].mean().round(1)
print(promedio_Ganacia_con_LeadStudio.head())


df_filtrado.to_csv("hollywood_limpio.csv")

