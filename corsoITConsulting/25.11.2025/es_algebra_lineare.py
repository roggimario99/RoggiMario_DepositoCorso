import numpy as np

A = np.array([[1,2],[3,4]])

A_inv = np.linalg.inv(A) #matrice inversa
print("Inversa: ", A_inv)

prodotto_dot = A.dot(A_inv)

print("verifica inversa: ", prodotto_dot )

v = np.array([1,2,3,4])
norm_v = np.linalg.norm(v)  #norma di un vettore
print("Norma di v: ", norm_v)

A = np.array([[1,2],[3,4]])
B = np.array([9,8])

x = np.linalg.solve(A,B)
print("soluzione del sistema lineare: ", x)

risultato = np.dot(A, x)
print("verifica risultato: ", risultato)



## trasformata di fourier

import numpy as np


# Creazione di un segnale

t = np.linspace(0, 1, 400)

sig = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)


# Calcolo della Trasformata di Fourier

fft_sig = np.fft.fft(sig)


# Frequenze associate

freqs = np.fft.fftfreq(len(fft_sig))


print("Trasformata di Fourier:", fft_sig)

print("Frequenze associate:", freqs)
