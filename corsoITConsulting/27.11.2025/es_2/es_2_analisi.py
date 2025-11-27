import pandas as pd
import numpy as np

#-------------------------------------------
#load dati
#-------------------------------------------

file_name = "prodotti_dataset.csv"
file_name = "prodotti_dataset_con_mancanti_e_duplicati.csv"
df = pd.read_csv(file_name)

print(df.head()) #visualizzazione prime righe

# ---------------------------------------------------
# Identificare e rimuovere eventuali duplicati
# ---------------------------------------------------
duplicati = df.duplicated()
print(f"Numero di righe duplicate: {duplicati.sum()}")
if duplicati.sum() > 0:
    df = df.drop_duplicates()  # elimino i duplicati
    print("DataFrame dopo rimozione duplicati:")
    print(df)
    print("duplicati eliminati!")
print("-" * 60)

# ---------------------------------------------------
# valori mancanti
# ---------------------------------------------------

numeriche = df.select_dtypes(include = ["int64", "float64"])

num_nan = df.isna().any(axis=1).sum()
print("-"*60)
print(f"Ci sono {num_nan} righe contenenti almeno un NaN.")

if num_nan > 0:
    for col in numeriche.columns:
        df[col].fillna(df[col].median(), inplace=True)
    
    print("DataFrame dopo imputazione dei NaN con la mediana:")
    print(df)
    print("-" * 60)

    df = df.dropna()
    
    print("DataFrame dopo eliminazione righe con nan non numeriche: ")
    print(df)
    print("-" * 60)

#-------------------------------------------
#nuova colonna
#-------------------------------------------

df["Totale Vendite"] = df["Quantità"] * df["Prezzo Unitario"]

#-------------------------------------------
#group by
#-------------------------------------------

# per prodotto
prodotti = df["Quantità"].groupby(df["Prodotto"]).sum()

print(f"Il prodotto più venduto è: {prodotti.idxmax()}")

# per citta

citta = df["Quantità"].groupby(df["Città"]).sum()

print(f"La città dove sono state registrate più vendite è: {citta.idxmax()}")


myTrashold = df["Totale Vendite"].mean() + df["Totale Vendite"].std()
df_filtrato = df[df["Totale Vendite"] > myTrashold ]

print("-"*60)
print("data frame filtrato:")
print(df_filtrato)

#sorting del dataframe

df_sorted = df.sort_values(by='Totale Vendite', ascending=False)

print("-"*60)
print("data frame ordinato tramite Tot vendite:")
print(df_sorted)

