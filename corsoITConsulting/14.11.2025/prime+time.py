import time

N_TOT = 0

def computeTime(func):
    
    def wrapper(*args, **kwargs):
        
        start = time.time()
        risultato = func(*args, **kwargs)
        end = time.time()
        print(f"La funzione '{func.__name__}' ha impiegato {(end - start)*1e3 :.10f} millesimi di secondo.")
        return(risultato)
    
    return(wrapper)

@computeTime
def is_prime(num):
    if num <=1:
        return False
    
    if num == 2:
        return True
    
    for j in range(2,int(num**0.5) + 1): #verifico per tutti i num maggiori di 1 che non abbiano divisori diversi da 1 e se stessi. 
        if num % j == 0:                 #j rappresenta i possibili divisori.
            return False                 #se trovo un divisore mi fermo e returno False                       
    return True

is_prime(N_TOT)