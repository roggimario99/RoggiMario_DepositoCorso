import pandas as pd
import numpy as np

file_path = "titanic.csv"

### Import del csv come DataFrame
df = pd.read_csv(file_path)

### Visualizzazione di alcune righe

print(df.head()) #prime 5 righe

print(df.tail()) #ultime 5 righe

# ---------------------------------------------------
# 3. Visualizzare il tipo di dati di ciascuna colonna
# ---------------------------------------------------
print("TIPI DI DATO DELLE COLONNE (dtypes):")
print(df.dtypes)
print("-" * 60)

# ---------------------------------------------------
# 4. Statistiche descrittive per colonne numeriche
#    (media, mediana, deviazione standard)
# ---------------------------------------------------
numeriche = df.select_dtypes(include=["float64", "int64"])
print(numeriche)
statistiche = numeriche.agg([np.mean, "median", "std"])  #agg is a function to use for aggregating the data
                                                         #accepts functions and function namesor a list of those

print("STATISTICHE DESCRITTIVE (colonne numeriche):")
print(statistiche)
print("-" * 60)

# ---------------------------------------------------
# 5. Identificare e rimuovere eventuali duplicati
# ---------------------------------------------------
duplicati = df.duplicated()
print(f"Numero di righe duplicate: {duplicati.sum()}")
df = df.drop_duplicates()  # elimino i duplicati
print("DataFrame dopo rimozione duplicati:")
print(df)
print("-" * 60)

# ---------------------------------------------------
# 6. valori mancanti
# ---------------------------------------------------


for col in numeriche.columns:
    df[col].fillna(df[col].median(), inplace=True)
   
print("DataFrame dopo imputazione dei NaN con la mediana:")
print(df)
print("-" * 60)

def classifica_eta(age):
    if 0 <= age <= 18:
        return "giovane"
    
    if 19 <= age <= 65:
        return "adulto"
    
    if age >= 65:
        return "senior"
    
df["Categoria Età"]  = df["Age"].apply(classifica_eta)

# ---------------------------------------------------
# 8. Salvare il DataFrame pulito in un nuovo file CSV
# ---------------------------------------------------
nome_file = "titanic_pulito.csv"
df.to_csv(nome_file, index=False, encoding="utf-8")
print(f"DataFrame pulito salvato in '{nome_file}'.")