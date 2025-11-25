import numpy as np

def creazione_matrice():  #richiede in imput le dimensioni e crea la matrice
    while True:
        
        n_righe = int(input("Inserire il num. di righe: "))
        if n_righe > 0:
            break
        else:
            print("il valore deve essere positivo!")
            
    while True:
        
        n_col = int(input("Inserire il num. di colonne: "))
        if n_righe > 0:
            break
        else:
            print("il valore deve essere positivo!")    
            
    mat = np.random.rand(n_righe, n_col)   #matrici con dimensioni nserite dall'utente din numeri random fra 0 e 1.
    
    return mat
    

def sottomatrice_centrale(mat):
    n_righe, n_col = mat.shape
    
    if n_righe < 3 or n_col < 3:
        raise ValueError("La matrice è troppo piccola.")
    
    # Calcolo dei limiti (25% - 75%)
    r_start = n_righe // 4
    r_end   = (3 * n_righe) // 4
    c_start = n_col // 4
    c_end   = (3 * n_col) // 4

    return mat[r_start:r_end, c_start:c_end]


def scrivi_dati(nome_file, dati, mode="w"):
    """Scrivi i dati in modo leggibile"""
    with open(nome_file, mode) as file:
        file.write(np.array2string(dati) )  # stampo l'array trasformato in stringa.
        file.write("\n")
        
def det(mat):
    
    if mat.shape[0] != mat.shape[1]:
        print("La matrice non è quadrata! Non posso fare il determinante.")
        
    else:
        return np.linalg.det(mat)

        





