import numpy as np

N = 50
arr_1 = np.linspace(0, 1, N)

def genera_dati():
    """Genera arr_2 e arr_sum."""
    arr_2 = np.random.rand(N)
    return arr_1 + arr_2

def scrivi_dati(nome_file, dati, mode="w"):
    """Scrivi i dati in modo leggibile utilizzando numpy.savetxt."""
    with open(nome_file, mode) as file:
        file.write(" ".join(map(str, dati)) + "\n")  # stampo l'array trasformato in stringa. Map fa un array di stringhe. join le unisce.

N_files = 1

# Primo file
arr_sum = genera_dati()
scrivi_dati("I_miei_dati.txt", arr_sum)

while True:
    print("\nE' stato creato il primo file di dati!")
    print("### MENU' ###")
    print("1. Aggiungere dati allo stesso file.")
    print("2. Sovrascrivere file.")
    print("3. Creare un nuovo file.")
    print("4. Esci.")

    scelta = input("Cosa vuoi fare? ")

    match scelta:
        case "1":
            arr_sum = genera_dati()
            scrivi_dati("I_miei_dati.txt", arr_sum, mode="a")

        case "2":
            arr_sum = genera_dati()
            scrivi_dati("I_miei_dati.txt", arr_sum, mode="w")

        case "3":
            arr_sum = genera_dati()
            nome = f"I_miei_dati_{N_files}.txt"
            scrivi_dati(nome, arr_sum, mode="w")
            N_files += 1

        case "4":
            break

        case _:
            print("Risposta non valida.")
            continue

    input("Operazione completata. Premi Invio per continuare...")

            