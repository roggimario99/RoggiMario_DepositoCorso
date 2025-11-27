import numpy as np
import pandas as pd

df = pd.read_csv("vendite_fittizie.csv")


pivot_df = df.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')

print(pivot_df)

prodotti = df.groupby("Prodotto")["Vendite"].sum()

print(prodotti)