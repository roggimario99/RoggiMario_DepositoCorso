import numpy as np
import pandas as pd

df = pd.read_csv("dataset_clienti_churn.csv")

print(df.info())
print(df.head())


# 1. Rimuovi righe dove ID_Cliente è NaN
df = df[df["ID_Cliente"].notna()]

# 2. Riempi tutti gli altri valori mancanti 
# (qui uso ad esempio la media per numerici e la moda per categorici)

for col in df.columns:
    if col != "ID_Cliente":   # non tocco l'ID
        if df[col].dtype != "object":
            df[col].fillna(df[col].median(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)
            
print(df.head())  

#nuove colonne

df["Costo_per_GB"] = df["Tariffa_Mensile"] / df["Dati_Consumati"]
df["Costo_per_contatto"] = df["Tariffa_Mensile"] / df["Servizio_Clienti_Contatti"]    

# Analisi di churn per segmento di età

durata_abbonamento_per_eta = df.groupby("Durata_Abbonamento")["Età"].mean()  
tariffa_per_eta = df.groupby("Tariffa_Mensile")["Età"].mean() 
dati_cons_per_eta = df.groupby("Dati_Consumati")["Età"].mean()
churn_per_eta = df.groupby("Churn")["Età"].mean()
churn_per_durata = df.groupby("Churn")["Durata_Abbonamento"].mean()
churn_per_tariffa = df.groupby("Churn")["Tariffa_Mensile"].mean()
churn_per_dati = df.groupby("Churn")["Dati_Consumati"].mean()

print("Durata abbonamento per età:")
print(durata_abbonamento_per_eta)   
print("Tariffa mensile per età:")
print(tariffa_per_eta)
print("Utilizzo dati GB per età:")
print(dati_cons_per_eta)
print("Churn per età:")
print(churn_per_eta)
print("Churn per durata abbonamento:")
print(churn_per_durata)
print("Churn per tariffa mensile:")
print(churn_per_tariffa)
print("Churn per utilizzo dati GB:")
print(churn_per_dati)
