from esercizio2 import Libro #importo la classe libro

class Biblioteca:
    def __init__(self, libri = []):  #costruttore
        self.libri = libri      #l'attributo è una lista di libri
        
    def aggiungi_libro(self, titolo, autore, pagine):
        self.libri.append(Libro(titolo, autore, pagine))  #puoi aggiungere un nuovo libro alla biblioteca
        
    def catalogo(self):  #stampa tutti i libri bnella biblioteca
        print("\n### Catalogo ###\n")
        for libro in self.libri: 
            print("--  ",libro)
            print()
            
            
biblioteca = Biblioteca()
biblioteca.aggiungi_libro("pizza","Antonino", 200)
biblioteca.aggiungi_libro("QED","R.P. Feynman", 195)
biblioteca.aggiungi_libro("Il nome della rosa","U. Eco", 500)

biblioteca.catalogo()