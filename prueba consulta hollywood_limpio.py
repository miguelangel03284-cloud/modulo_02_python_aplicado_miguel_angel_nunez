import pandas as pd

df = pd.read_csv("hollywood_limpio.csv")

print(df.shape)
print("-------------------------------------------------------")
print(df.head())
print("-------------------------------------------------------")
print(df. columns)
print("-------------------------------------------------------")
print(df.isnull().sum())
