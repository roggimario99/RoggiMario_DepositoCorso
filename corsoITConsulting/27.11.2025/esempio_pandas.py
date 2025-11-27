import pandas as pd

file_path = "file_vendite.csv"

df = pd.read_csv(file_path)

print(df.head())

data = {
    "nome": ["Alice", "Bob", "Carla"],
    "Età": [25, 30, 22],
    "Città": ["Roma", "Milano", "Napoli"]
}

df = pd.DataFrame(data)

# stampa data frame
print(df)

#selezione righe
df_older = df[df["Età"] > 23]

#stampa delle righe selezionate
print("\nPersone con età > di 23")
print(df_older)


df["Maggiorenne"] = df["Età"] >= 18

# stampa data frame aggiornato
print(df)