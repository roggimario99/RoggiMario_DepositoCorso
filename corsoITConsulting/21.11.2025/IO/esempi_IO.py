file = open("prova.txt", "r")
contenuto = file.read()
riga = file.readline() 

print(contenuto)

file.close() #sempre chiudere il file dopo averlo usato

file = open("prova.txt", "w") #apre il file in scrittura, se esiste gia' cancella tutto il contenuto
file.write("Ciao sono Mario") #scrive nel file
file.close()

newFile = open("prova_nuovo.txt", "w") #se apri un file non esistente lo crea!
newFile.write("Ciao sono sempre io!") #scrive nel file
newFile.close()

#-------------------------------------------------------
#  utilizzo di with
#-------------------------------------------------------

with open("prova.txt", "r") as file:
    contenuto = file.read()
    
    print(contenuto)
