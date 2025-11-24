def is_larger_vector(myList):
    res = []
    for i in range(len(myList)-2):
        res.append( bool(myList[i] + myList[i+1] > myList[i+2]) )  
    
    res.append(bool( 2*myList[-2] > myList[-1])  ) #penultimo elemento utilizzo se stesso due volte
    res.append( True ) #l'ultimo lo metto sempre vero
    
    return res

        
def is_larger(i):

    return bool(myList[i] + myList[i+1] > myList[i+2]) 
    
    res.append(bool( 2*myList[-2] > myList[-1])  ) #penultimo elemento utilizzo se stesso due volte
    res.append( True ) #l'ultimo lo metto sempre vero
    
    return res        
        
        
numbers = [1,4,2,3,7,1,3,5,6]
filtered_numbers = list(filter(is_larger, numbers))

print( filtered_numbers )
    