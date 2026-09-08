import pandas as pd

df = pd.read_csv("hollywood.csv")

# print(df.shape)
# print(df.head())

df_filtrado = df[["Movie", "LeadStudio", "Genre", "RottenTomatoes",	"AudienceScore",
"WorldGross", "Budget",	"Year"]]

print(df_filtrado.shape)

print(df_filtrado.isnull().sum())
