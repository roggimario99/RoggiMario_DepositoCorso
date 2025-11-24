import random

N = 40
numbers = [*range(N)]
#random.shuffle(numbers)

# funzione di filtro: prende un indice x
def sum_greater_then_next(x):
    
    """Implementa la condizione el_x + el_x+1 > el_x+2 con condizione cicliche all'estremo dell'array!"""
    if x == (len(numbers) - 2): 
        return numbers[-1] + numbers[0] > numbers[1] #penultimo elemento 
    
    elif x == (len(numbers) - 1): 
        return numbers[-2] + numbers[-1] > numbers[1] #ultimo elemento
    
    else:
        return numbers[x] + numbers[x + 1] > numbers[x + 2] #condizione standard
        



indici = range( len(numbers) )

indici_validi = list( filter(sum_greater_then_next, indici) )

array_filtrato = [
    numbers[i] for i in indici_validi
]


print("Array di partenza:", numbers) 
print("Indici validi:", indici_validi) 
print("Array filtrato:", array_filtrato) 

