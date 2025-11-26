from analyzers import *
import numpy as np

file = open("results.txt","w")
file.close

dic = {"si": True, "no": False}

file_1d = "dati1d_random.txt" 
file_2d = "dati2d_random.txt" 

arr = np.loadtxt("dati1d_random.txt")
mat = np.loadtxt("dati2d_random.txt")

while True:
    nome_file = input("inserisci il nome del file: ")
    if nome_file.split(".")[-1] == "txt":
        data =np.load(nome_file)
        
    
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
            stat_analysys(mat)
            
        case "2":
            pos_analysys(mat)
            
        case "3":
            by_axis_analysys(arr)
            
        case "4":
            matrix_analysys(mat, mat.T)
                
        case "0":
            break

        case _:
            print("Risposta non valida.")
            continue

    input("Operazione completata. Premi Invio per continuare...")