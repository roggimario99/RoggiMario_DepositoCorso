import sqlite3
import csv

# Nomi dei file
DB_NAME = 'california_housing.db'
CSV_FILE = 'california_housing_data.csv'


# --- 1. FUNZIONE PER IMPORTARE CSV NEL DB ---
def importa_csv_in_db():
    print("\n--- Inizio Importazione CSV -> SQLite ---")
    
    # Connessione al DB
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # 1. Creiamo la tabella (se non esiste)
    # Nota: Definiamo i tipi corretti (REAL per prezzi, INTEGER per quantità)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS housing (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        MedInc REAL,
        HouseAge REAL,
        AveRooms REAL,
        AveBedrms REAL,
        Population REAL,
        AveOccup REAL,
        Latitude REAL,
        Longitude REAL,
        MedHouseVal REAL
        
    );
    """)

    # 2. Apertura e Lettura del CSV
    with open(CSV_FILE, mode='r', encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        
        # IMPORTANTE: Saltiamo l'intestazione (header) del CSV
        # next() legge la prima riga e sposta il cursore alla seconda
        header = next(csv_reader) 
        print(f"Header rilevato: {header}")

        # 3. Preparazione dei dati (TRANSFORM)
        # Il CSV legge tutto come stringhe. Dobbiamo convertire i numeri.
        dati_da_inserire = []
        for riga in csv_reader:
            dati_di_riga = []
            # riga è tipo ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', ..., 'MedHouseVal']
            for parametro in riga:
                try:
                    val = float(parametro)
                    dati_di_riga.append(val)
                    
                except:
                    print(f"Saltata riga corrotta: {riga}")
            dati_da_inserire.append(dati_di_riga)

        # 4. Inserimento di massa (LOAD)
        # Usiamo executemany per la massima velocità
        sql = """INSERT INTO housing (MedInc, HouseAge, AveRooms, 
        AveBedrms, Population, AveOccup, 
        Latitude, Longitude, MedHouseVal) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.executemany(sql, dati_da_inserire)
        
        conn.commit()
        print(f"Importati con successo {cursor.rowcount} houses blokcs.")

    conn.close()
    
importa_csv_in_db()