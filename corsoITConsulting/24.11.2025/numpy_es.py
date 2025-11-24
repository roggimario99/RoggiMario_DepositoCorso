import numpy as np
import pandas as pd

x = np.array([1,2,3,4,5,6,7,8,9])    #istanziazione array
print("dim: ",x.shape[0])

x = np.array([[1,2,3,4],[5,6,7,8]])   #istanziazione array bidimensionale
print("dim: ",x.shape)

# Creazione di un array
arr = np.array([1, 2, 3, 9, 5])

# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape) # Output: (5,), il numero di colonne è uno ed è lasciato implicito
print("Dimensioni dell'array:", arr.ndim) # Output: 1
print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma)
print("Numero di elementi:", arr.size) # Output: 5
print("Somma degli elementi:", arr.sum()) # Output: 15
print("Media degli elementi:", arr.mean()) # Output: 3.0
print("Valore massimo:", arr.max()) # Output: 5
print("Indice del valore massimo:", arr.argmax()) # Output: 4

array_di_zeri = np.zeros(9)  #lunghezza 9
print(array_di_zeri)

array_di_zeri = np.zeros((2,3))  #forma (2,3)
print(array_di_zeri)

#x = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12,13]]) #errore! Non puoi array con righe con dim diverse  

# arrange

arr = np.arange(3,14,2)
print(arr)
arr = arr.reshape((3,2))
print(arr)

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