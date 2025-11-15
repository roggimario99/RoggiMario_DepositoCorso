from esercizio_riassuntivo import dado

def logDado(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        
        print(f"Il risultato del tiro è: {res}")
        return(res)
    return wrapper

dado = logDado(dado)

dado()

def sum_prod(func):
    def wrapper(*args, **kwargs):
        sum, dif = func(*args, **kwargs)
        x = (sum + dif)/2
        y = (sum - dif)/2
        
        return x + y, x * y
                
    return(wrapper)           
 
 
@sum_prod   
def sum_prod_bad (x, y):
    return x + y, x - y     

print( sum_prod_bad(2,5) )