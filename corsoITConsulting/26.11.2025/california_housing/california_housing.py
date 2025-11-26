import numpy as np
import sqlite3

DB_NAME = "california_housing.db"

#---------------------------------
#import da csv
#---------------------------------

nome_file = "california_housing_data.csv"
data = np.loadtxt(nome_file, delimiter=",", skiprows=1)
with open(nome_file, "r") as f:
    headers = f.readline().strip().split(",")
    
#---------------------------------
#import da db
#---------------------------------

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

print("\n--- Lettura di tutti i libri ---")
cursor.execute("SELECT * FROM housing")

# fetchall() recupera tutte le righe rimanenti come una lista di tuple
data_from_db = cursor.fetchall()

conn.close()

data_from_db_np_array = np.array(data_from_db)
data = data_from_db_np_array[:,1:] #elimino colonna indici

min_val = np.min(data, axis = 0)   
max_val = np.max(data, axis = 0)
mean = np.mean(data, axis = 0)
std = np.std(data, axis = 0)
ind_val_min = np.argmin(data, axis = 0)    
ind_val_max = np.argmax(data, axis = 0)
mediana = np.percentile(data, 50, axis = 0)

"""print(f"headers: {' '.join(headers)}\n")
print(f"min: {' '.join(map(str, min_val))}")
print(f"max: {' '.join(map(str, max_val))}")
print(f"mean: {' '.join(map(str, mean))}")
print(f"standard deviation: {' '.join(map(str, std))}")
print(f"indice del val min: {' '.join(map(str, ind_val_min))}")
print(f"indice del val max: {' '.join(map(str, ind_val_max))}")
print(f"median: {' '.join(map(str, mediana))}")"""

print(f"headers: {headers}\n")

#---------------------------------
#salva file
#---------------------------------

with open("results.txt", "w") as file:
    file.write(f"headers: {' '.join(headers)}\n")
    file.write("\n")
    file.write(f"min: {' '.join(map(str, min_val))}\n")
    file.write(f"max: {' '.join(map(str, max_val))}\n")
    file.write(f"mean: {' '.join(map(str, mean))}\n")
    file.write(f"standard deviation: {' '.join(map(str, std))}\n")
    file.write(f"indice del val min: {' '.join(map(str, ind_val_min))}\n")
    file.write(f"indice del val max: {' '.join(map(str, ind_val_max))}\n")
    file.write(f"median: {' '.join(map(str, mediana))}\n\n")
    

#---------------------------------
#salva in db
#---------------------------------

DB_NAME = "results"

def crea_db_risultati():
    print("\n--- Inizio Importazione CSV -> SQLite ---")
    
    # Connessione al DB
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # 1. Creiamo la tabella (se non esiste)
    # Nota: Definiamo i tipi corretti (REAL per prezzi, INTEGER per quantità)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quantity TEXT NOT NULL,
        min_val  REAL,
        max_val  REAL,   
        mean     REAL,
        std      REAL,
        ind_val_min    REAL, 
        ind_val_max    REAL,
        mediana REAL
        
    );
    """)
    
    quantity = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude', 'MedHouseVal']
    risultati = []
    risultati.append(quantity)



    risultati.append(min_val.tolist())
    risultati.append(max_val.tolist())
    risultati.append(mean.tolist())
    risultati.append(std.tolist())
    risultati.append(ind_val_min.tolist())
    risultati.append(ind_val_max.tolist())
    risultati.append(mediana.tolist())

    risultati = np.array(risultati).T.tolist()
    
    # 4. Inserimento di massa (LOAD)
    # Usiamo executemany per la massima velocità
    sql = """INSERT INTO results (quantity, min_val, max_val, mean, std, ind_val_min, 
            ind_val_max, mediana) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor.executemany(sql, risultati)

    conn.commit()
    print(f"Importati con successo {cursor.rowcount} statistiche.")

    conn.close()

crea_db_risultati()


