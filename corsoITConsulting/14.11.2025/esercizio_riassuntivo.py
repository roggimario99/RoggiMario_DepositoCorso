#Scrivere un programma che simuli un gioco da tavolo con un numero di giocatori a scelta dell'utente (fra 2 e 6).
#se il giocatore dopo aver tirato si trova su una casella che è un primo o appartiene alla serie di fibonacci può tirare di nuovo.
#Il gioco ha un tabbellone con 50 caselle. 
#A ogni turno un giocatore tira un dado a sei facce e fa tanti passi quanto il numero il primo che arriva vince.
#A ogni turno il codice deve printare un riassunto del turno (pos di ogni giocatore) e alla fine dire chi aha vinto e quanti turni è durato il gioco.

import random


def dado():                       #dado a sei facce
    return random.randint(1,6)

def numPlayers():                 #funz. che richiede in inmput il numero di giocatori
    num = 0
    while num < 2 or num > 6:
        num = int(input("Quanti giocatori vuoi? (fra 2 e 6): "))
    return num

def posIniziali(players):
    pos_0 = []
    for i in range(players):
        pos_0.append(0)
    return pos_0

def max40(numero):
    if numero >= 40:
        return 40
    else:
        return numero
    
def riassunto(players,turno,pos):
    print(f"Turno: {turno}")
    for i in range(players):
        pos[i] = max40(pos[i])
        print(f"Il giocatore {i} è nella casella {pos[i]}") 
    print("\n\n")

def riassuntoFin(turno, vincitore):
    if len(vincitore) == 1:
        print(f"Il gioco è durato {turno} turni ed è stato vinto dal giocatore {vincitore[0]}.")
    else:
        print(f"Hanno vinto a parimerito i giocatori: ", end="")
        for v in vincitore[:-1]:
            print(f"{v}, ", end="")
        print(f"e {vincitore[-1]}.", end = "\n\n")

def is_prime(num):
    if num <=1:
        return False
    
    if num == 2:
        return True
    
    for j in range(2,int(num**0.5) + 1): #verifico per tutti i num maggiori di 1 che non abbiano divisori diversi da 1 e se stessi. 
        if num % j == 0:                 #j rappresenta i possibili divisori.
            return False                 #se trovo un divisore mi fermo e returno False                       
    return True

def fibbonacci(N, a = 1, b = 1):  
    n_in_seq = [a,b] #definisco una lista con i primi due valori della sequenza

    while n_in_seq[-1] + n_in_seq[-2] < N:
        n_in_seq.append(n_in_seq[-1] + n_in_seq[-2]) #aggiungo il numero alla sequenza come somma dei due precedenti                                   
        
    return n_in_seq                                 #returno la sequenza


##inizio gioco
while(True): #possibilità di fare più partite consecutive se l'utennbgte vuole
 
    ## partita
    players = numPlayers()
    pos = posIniziali(players)
    turno = 1
    vincita = False
    vincitore = []
    fib_100 = fibbonacci(100) #primi 100 val della seq di fibbonacci
    
    while not vincita:
        for i in range(players):
            pos[i] += dado()
            if pos[i] in fib_100 or is_prime (pos[i] ):  
                pos[i] += dado()  
            if pos[i] >= 40:
                vincita = True
                vincitore.append(i)
        riassunto(players, turno, pos)
        if vincita:
            riassuntoFin(turno, vincitore)
        else:    
            turno += 1
        pass
        
    rep = input("Vuoi ripetere? (si/no): ")
    if rep == "no":
        break
    elif rep == "si":
        continue
    else:
        print("ERRORE! Risposta non valida.")
        break
        