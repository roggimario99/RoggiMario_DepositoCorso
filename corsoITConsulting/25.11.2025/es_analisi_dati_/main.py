from analyzers import *
import numpy as np

file = open("results.txt","w")
file.close

dic = {"si": True, "no": False}


#----------------------------------------------
#load dei dati
#----------------------------------------------

nome_file = input("inserisci il nome del file: ")
data = data_load(nome_file)

while True:
    

    #----------------------------------------------
    #MENU
    #----------------------------------------------
    
    print("### MENU' ###")
    print("1. Analisi statistiche di base (1D).")
    print("2. Analisi posizionale (1D).")
    print("3. Analisi per assi (2D).")
    print("4. Operazioni matriciali e algebbriche (2D).")
    print("0. Esci.")

    scelta = input("Cosa vuoi fare? ")
    
    if scelta != "0":
        print_file = input("Vuoi stampare su file? (si/no): ")
        
        while print_file.lower().strip() not in ("si", "no"):
            print_file = input("Risposta non valida. rispondi si o no: ")
        print_file = dic[print_file.lower().strip()]

    match scelta:
        case "1":
            stat_analysys(data)
            
        case "2":
            pos_analysys(data)
            
        case "3":
            by_axis_analysys(data)
            
        case "4":
            nome_file = input("inserisci il nome del file da cui importare la matrice con cui fare il prodotto: ")
            data_bis = data_load(nome_file)
            matrix_analysys(data, data_bis)
                
        case "0":
            break

        case _:
            print("Risposta non valida.")
            continue

    input("Operazione completata. Premi Invio per continuare...")