import numpy as np

a = 1
b = 100
shape = (6,6)

mat = np.random.randint(a, b + 1, shape)  #array di dim. shape di interi random fra a e b

print("matrice originale: \n", mat, "\n")
print("Sottomatrice centrale 4x4: \n", mat[1:5, 1:5], "\n")


i = np.arange(-1, -mat.shape[0] - 1, -1) # [-1 -2 -3 -4 -5 -6]

mat_ivertita = mat[i]
print("matrice con righe invertite: \n", mat_ivertita, "\n")
mat_ivertita = mat[::-1,:]
print("matrice con righe invertite: \n", mat_ivertita, "\n")

diagonale = np.diag(mat)
print("Diagonale: ", diagonale)

i = np.arange( mat.shape[0] )
diagonale = mat[[i],[i]]
print("Diagonale: ", diagonale)

mat_fin = mat.copy()
mat_fin [ mat % 3 == 0] = 99
print("Matrice modificata con maschera booleana: ", mat_fin)

