import numpy as np
print("\n=== 6) Broadcasting 3D: matrice 2D + vettore 1D ===")
M = np.ones((2, 3, 4))    # shape (2,3,4)
print(M)
v = np.array([1, 2, 3, 4]) # shape (4,)
print("M shape:", M.shape)
print("v shape:", v.shape)
print("M + v =\n", M + v)
# v viene applicato all'ultima dimensione