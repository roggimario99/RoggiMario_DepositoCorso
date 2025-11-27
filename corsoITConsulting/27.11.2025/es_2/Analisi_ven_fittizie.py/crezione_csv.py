import numpy as np
import pandas as pd

dict_dati = {"Data": [], "Città": [], "Vendite": [], "Prodotto": []}

N = 200
citta_varie = ["Roma", "Roma", "Milano", "Cava De' Tirreni", "Milano", "Milano"]
prodotti_vari = ["cellulare", "computer", "penna", "penna"]

for _ in range(N):
    citta = np.random.choice(citta_varie)
    prodotto = np.random.choice(prodotti_vari)
    vendite = np.random.randint(100, 1001)
    giorno = np.random.randint(1,31)
    data = f"{giorno}-11-2025"
    
    dict_dati["Città"] += [citta]
    dict_dati["Prodotto"] += [prodotto]
    dict_dati["Vendite"] += [vendite]
    dict_dati["Data"] += [data]
    
df = pd.DataFrame(dict_dati)

df.to_csv("vendite_fittizie.csv")


    
    
    