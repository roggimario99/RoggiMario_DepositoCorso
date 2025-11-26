import numpy as np

N = 1000

M = 20

name = "dati1d_random.txt"

array = np.random.uniform(-1,1,N)
with open(name, "w") as file:
        np.savetxt(name, array)
        
name = "dati1d_random.csv"

array = np.random.uniform(-1,1,N)
with open(name, "w") as file:
        np.savetxt(name, array, delimiter=";") 
        
name = "dati2d_random.txt"        
array = np.random.uniform(-1,1,4*M)
mat = array.reshape(4,M)
with open(name, "w") as file:
        np.savetxt(name, mat)
        
name = "dati2d_random.csv"        
array = np.random.uniform(-1,1,4*M)
mat = array.reshape(4,M)
with open(name, "w") as file:
        np.savetxt(name, mat, delimiter=";")
                
        
