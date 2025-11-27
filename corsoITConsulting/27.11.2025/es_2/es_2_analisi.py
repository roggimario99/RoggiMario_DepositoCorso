import pandas as pd
import numpy as np

#-------------------------------------------
#load dati
#-------------------------------------------

file_name = "prodotti_dataset.csv"
df = pd.read_csv(file_name)

print(df.head()) #visualizzazione prime righe

#-------------------------------------------
#nuova colonna
#-------------------------------------------

df["Totale vendite"] = df["Quantità"] * df["Prezzo Unitario"]

#-------------------------------------------
#group by
#-------------------------------------------

# per prodotto
prodotti = df["Quantità"].groupby(df["Prodotto"]).sum()

print(f"Il prodotto più venduto è: {prodotti.idxmax()}")

print(prodotti[np.argmax(prodotti)])

# per citta

citta = df["Quantità"].groupby(df["Città"]).sum()

print(f"La città dove sono state registrate più vendite è: {citta.idxmax()}")


myTrashold = df["Totale vendite"].mean() + df["Totale vendite"].std()
df_filtrato = df[df["Totale vendite"] > myTrashold ]


print(df_filtrato)