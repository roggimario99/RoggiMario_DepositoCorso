#---------------------------------------------------
#CLASSE LIBRO
#---------------------------------------------------
             
class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn
        
    def descrizione(self):
        '''Stampa descrizione del libro.'''
        
        print(f"Il libro {self.titolo} è scritto da {self.autore} e ha isbn: {self.isbn}.")
        
    def __str__(self):
        """Returna una stringa con le caratteristiche del libro."""
        
        return f"Titolo: {self.titolo}, autore: {self.autore}, isbn: {self.isbn}."

#---------------------------------------------------
#CLASSE LIBRERIA
#---------------------------------------------------    

class Libreria:
    def __init__(self, catalogo = []):
        self.catalogo = catalogo
        self.titoli =[]     #lista titoli
        self.isbn = []      #lista.isbn

        for libro in self.catalogo:
            self.titoli.append(libro.titolo)
            self.isbn.append(libro.isbn)
            
    
        
    def aggiungi_libro(self, libro): 
        '''aggiunge libro per titolo'''
        
        if libro.titolo not in self.titoli:
            self.catalogo.append(libro)
            print("Libro aggiunto!")
        else:
            print("Libro già in catalogo")
            
    def rimuovi_libro(self, isbn): 
        """rimuove libro per isbn"""
        
        for i in range(len(self.isbn)):
            if self.isbn[i] == isbn:
                self.catalogo.pop(i)
                
    def cerca_per_titolo(self, titolo):
        """trova tutti i libri con dato titolo"""
        
        libri_trovati = []
        for i in range(len(self.titoli)):
            if self.titoli[i] == titolo:
                libri_trovati.append(self.catalogo[i])
        return libri_trovati
        
    def mostra_catalogo(self):
        """Stampa il catalogo."""
        
        print("### CATALOGO ###")
        for libro in self.catalogo:
            print(libro)
        
        