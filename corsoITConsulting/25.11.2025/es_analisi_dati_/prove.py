import numpy as np

arr = np.loadtxt("dati1d_random.txt")
mat = np.loadtxt("dati2d_random.txt")

print(np.min(arr))
dim = len(mat.shape)
print(dim)
print(np.min(arr, axis = 0))
print(np.min(mat, axis = dim -1))

print(np.transpose(arr))
print(np.linalg.norm(arr))
print(np.cov(arr))
