import numpy as np

arr_0a49 = np.arange(0,50)
arr_random = np.random.randint(49,102,50)

myArr = np.concatenate((arr_0a49,arr_random))

print("array: ",myArr)
print("type: ",myArr.dtype)
print("shape: ",myArr.shape)

myArrFloat = myArr.astype("float")

print("type: ",myArrFloat.dtype)
print("shape: ",myArrFloat.shape)

#slicing

print("primi dieci: ", myArrFloat[:10])
print("ultimi 7: ", myArrFloat[-7:])
print("da 5 a 10: ", myArrFloat[5:10])
print("uno ogni 4: ", myArrFloat[::4])


myArrFloat[10:15] = 99

print("Array modificato: ", myArrFloat)

i = [0, 3, 7, 12, 25, 33, 48]

print("elementi in posizioni scelte: ", myArrFloat[i])

print("elementi pari: ", myArrFloat[ myArrFloat % 2 == 0])

media = np.mean(myArrFloat)
print("elementi maggiore della media: ", myArrFloat[ myArrFloat > media])