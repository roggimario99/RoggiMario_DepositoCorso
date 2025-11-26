import numpy as np

N = 1000
L = 4
M = 20

def create_file(name, array):
        if name.split(".")[-1] == "txt":
                with open(name, "w"):
                        np.savetxt(name, array)  

                
        if name.split(".")[-1] == "csv":
                with open(name, "w"):
                        np.savetxt(name, array, delimiter = ",")  


name = "dati1d_random.txt"
array = np.random.uniform(-1,1,N)
create_file(name, array)

name = "dati1d_random.csv"
array = np.random.uniform(-1,1,N)
create_file(name, array)
        
name = "dati2d_random.txt"        
array = np.random.uniform(-1,1,L*M)
array = array.reshape(L,M)
create_file(name, array)
        
name = "dati2d_random.csv"        
array = np.random.uniform(-1,1,L*M)
array = array.reshape(L,M)
create_file(name, array)
        
name = "dati1d_normal.txt"
array = np.random.normal(0,1,N)
create_file(name, array)