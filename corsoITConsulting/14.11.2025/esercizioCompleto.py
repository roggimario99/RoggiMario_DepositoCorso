def is_prime(num):
    if num <=1:
        return False

    for j in range(2,int(num**0.5) + 1): #verifico per tutti i num maggiori di 1 che non abbiano divisori diversi da 1 e se stessi. 
        if num % j == 0:                 #j rappresenta i possibili divisori.
            return False                 #se trovo un divisore mi fermo e returno False
                              
        
    return True


num = 0   #inizializzo n a 0
while num <= 0:                #ciclo finchè n è neg o nullo
    num = int(input("Inserisci un numero positivo: "))
    
sumPari = 0
for n in range(1, num + 1, 2):  #ciclo sui dispari
    sumPari += n+1     #sommo un pari alla somma dei prec
    print(n, end=" ")  #printo i dispari
print()         #vado a capo

if num%2 == 1:         #se il num inserito è dispari devo correggere la somma sottr num + 1
    sumPari -= num + 1

print(f"La somma dei pari da 1 a {n} è: {sumPari}")    

if is_prime(num):
    print(f"{num} è primo!")
else:
    print(f"{num} non è primo!")
    