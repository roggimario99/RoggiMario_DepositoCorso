import numpy as np

x = np.arange(1,26)

mat = x.reshape((5,5))

print(f"matrice: \n{mat}")

riga_2 = mat[1]
riga_3 = mat[2]
col_4 = mat[:,3]

print(f"riga_2: ",riga_2)
print(f"riga_3: ",riga_3)
print(f"col_4: ",col_4)

diag = np.diagonal(mat, -1)

print(f"diagonale: ",diag)

sum_diag = np.sum(diag)

print(f"somma elementi diagonale: ",sum_diag)