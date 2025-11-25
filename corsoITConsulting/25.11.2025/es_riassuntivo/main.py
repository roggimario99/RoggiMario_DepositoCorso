from esercizio_riassuntivo import *
import numpy as np

while True:
    
    n_righe = int(input("Inserire il num. di righe: "))
    if n_righe > 0:
        break
    else:
        print("il valore deve essere positivo!")
        
while True:
    
    n_col = int(input("Inserire il num. di colonne: "))
    if n_col > 0:
        break
    else:
        print("il valore deve essere positivo!")    
        
mat = np.random.rand(n_righe, n_col)   #matrici con dimensioni nserite dall'utente di numeri random fra 0 e 1.

nome_file = "my_data.txt"              #print su file
scrivi_dati(nome_file, mat, mode="w")

while True:
    print("### MENU' ###")
    print("1. Matrice centrale.")
    print("2. Trasposta.")
    print("3. Somma elementi")
    print("4. Media elementi")
    print("5. prodotto per una nuov matrice.")
    print("6. determinante.")
    print("7. Esci.")

    scelta = input("Cosa vuoi fare? ")

    match scelta:
        case "1":
            sott_centr = sottomatrice_centrale(mat)
            scrivi_dati(nome_file, sott_centr, mode="a")
            print("Sottomatrice aggiunta al file!")

        case "2":
            transp = np.transpose(mat)
            scrivi_dati("I_miei_dati.txt", transp, mode="a")
            print("transposta aggiunta al file!")


        case "3":
            arr_sum = np.sum(mat)
            with open(nome_file, "a") as file:
                file.write(f"la somma e': {arr_sum}")  # stampo l'array trasformato in stringa.
                file.write("\n")
                
        case "4":
            arr_mean = np.mean(mat)
            with open(nome_file, "a") as file:
                file.write(f"la media e': {arr_mean}")  # stampo l'array trasformato in stringa.
                file.write("\n")
                
        case "5":
            mat_2 = np.random.rand(n_righe, n_col) 
            mat_prod = mat * mat_2
            scrivi_dati("I_miei_dati.txt", mat_prod, mode="a")
        
        case "6":
            det = det(mat)
            with open(nome_file, "a") as file:
                file.write(f"Il determinate e': {det}")  # stampo l'array trasformato in stringa.
                file.write("\n")
                
        case "7":
            break

        case _:
            print("Risposta non valida.")
            continue

    input("Operazione completata. Premi Invio per continuare...")

            