from classe_contobancario import ContoBancario

conto = ContoBancario()

print("Buongiorno! Benvenuto alla registrazione per il tuo conto bancario.")
nome = input("Inserisci il tuo nome: ")
res = conto.set_titolare(nome)

while not res:
    print("Nome non valido! Inserisci nuovamente.")
    nome = input("Inserisci il tuo nome: ")
    res = conto.set_titolare(nome) 

saldo = int(input("Inserisci il tuo saldo attuale: ") )
res = conto.deposita(saldo)

while not res:
    print("Saldo non valido! Inserisci un valore positivo.")
    saldo = int(input("Inserisci il tuo saldo attuale: ") )
    res = conto.deposita(saldo)
    

    
    
while True:  #chiede all'utente se vuole ripetere le operazioni.
    azione = input("Che operazione vuoi fare oggi? \n (deposita: 1, preleva: 2, visualizza saldo: 3, esci: 4)\n Inserire numero: ")
    
    match azione:
        case "1":
            importo = int(input("Inserisci quanto vuoi depositare: ") )
            conto.deposita(importo)
            
        case "2":
            importo = int(input("Inserisci quanto vuoi prelevare: ") )
            conto.preleva(importo)
            
        case "3":
            conto.visualizza_saldo()
            
        case "4":
            break
        
        case _:
            print("Operazione non valida!")
    
    
    
    
    while True:
        scelta = input("Vuoi fare una nuova operazione? (si/no): ").strip().lower()
        if scelta in ("si", "no"):   #ripete se la risposta non è valida
            break
        print("Risposta non valida. Scrivi 'si' o 'no'.")

    if scelta == "no":
        break
