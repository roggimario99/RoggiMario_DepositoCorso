import numpy as np

a = 10
b = 50
size = 20
arr = np.random.randint(a, b + 1, size )  #array di un num size di interi random fra a e b

print(arr)
print("Primi 10 elementi: ",arr[:10])
print("ultimi 5 elementi: ",arr[-5:])
print("elementi dal 6° all'15° posto: ", arr[5:15])
print("ogni terzo elemento a partire dal primo: ",arr[::3])

arr[5:10] = 99 #assegno il val 99 agli elementi fra il 6° e il 10°
print("array modificato: ",arr)