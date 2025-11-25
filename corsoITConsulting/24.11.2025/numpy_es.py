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

