def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funz")
        funzione()
        print("dopo l'esecuzione della funz")
    return wrapper
        
@decoratore
def saluta():
    print("ciao!")
    
saluta()     

def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("prima")
        risultato = funzione(*args, **kwargs) 
        print("dopo")
        return risultato
    return wrapper
    
    
@decoratore_con_argomenti
def somma(a,b):
    print(a+b)
    return a+b

#print(f"Il ris è: {somma(3,4)}")
print(somma(2,3))