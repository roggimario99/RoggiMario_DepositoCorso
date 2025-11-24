import numpy as np

#### Indexing e slicing
x = np.array([[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]) 

print(x[0][2])  #3, prima riga terza colonna
print(x[0,2])  #3, prima riga terza colonna

print(x[0:2,:])  # slicing righe, prendo le prime due
print(x[:,1:3])  # slicing colonne, prendo la seconda e la terza -- secondo indice sempre escluso

print(x[0:2,1:])  # slicing misto

x = x.reshape((x.shape[0] * x.shape[1]))
print("\n\n")
print(x[x>5])  # slicing booleano



print("\n\n")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# Slicing di base

print(arr[2:7])  # Output: [2 3 4 5 6]


# Slicing con passo

print(arr[1:8:3])  # Output: [1 3 5 7]


# Omettere start e stop

print(arr[:5])  # Output: [0 1 2 3 4]

print(arr[5:])  # Output: [5 6 7 8 9]


# Utilizzare indici negativi

print(arr[-5:])  # Output: [5 6 7 8 9]

print(arr[:-5])  # Output: [0 1 2 3 4]

# fancy indexing

arr = np.array([10,20,30,40,50])

indeces = np.array([1,3])

print(arr[indeces])

