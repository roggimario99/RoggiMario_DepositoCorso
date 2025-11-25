import numpy as np

N = 12 #numero elementi
arr = np.linspace(0,1, N)

mat_1 = arr.reshape((3,4)) #reshape
print("mat_1: \n",mat_1)


mat_2 = np.random.rand(3,4) #matrice random

print("-"*30)
print("mat_2: \n",mat_2)

mat_sum = mat_1 + mat_2           #sum


print("-"*30)
print("mat_1 + mat_2: \n", mat_sum) 

mat_sum = np.add(mat_1, mat_2)     #funzione add, fa lo stesso

print("-"*30)
print("mat_1 + mat_2 (con np.add): \n", mat_sum) 