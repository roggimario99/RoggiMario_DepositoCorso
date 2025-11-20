from abc import ABC, abstractmethod

# ======================================
# Classe astratta Impiegato
# ======================================
class Impiegato(ABC):
    
    def __init__(self, nome, cognome, stipendio_base):
       self.nome = nome
       self.cognome = cognome
       self.stipendio_base = stipendio_base
    
    @abstractmethod
    def calcola_stipendio(self):
        pass


# ======================================
# Impiegato a stipendio fisso
# ======================================
class ImpiegatoFisso(Impiegato):
    def calcola_stipendio(self):
        return self.stipendio_base


# ======================================
# Impiegato a provvigione
# ======================================
class ImpiegatoAProvvigione(Impiegato):
    def __init__(self, nome, cognome, stipendio_base, vendite):
        super().__init__(nome, cognome, stipendio_base)
        self.vendite = vendite

    def calcola_stipendio(self):
        return self.stipendio_base + self.vendite * 0.1


# ======================================
# Funzione richiesta: stampa info impiegato
# ======================================
def stampa_impiegato(imp):
    print(f"Impiegato: {imp.nome} {imp.cognome}")
    print(f"Stipendio base: {imp.stipendio_base} €")
    print(f"Stipendio calcolato: {imp.calcola_stipendio()} €")
    print("-" * 30)


# ======================================
# Esempio d'uso
# ======================================
if __name__ == "__main__":
    i1 = ImpiegatoFisso("Mario", "Rossi", 1500)
    i2 = ImpiegatoAProvvigione("Luca", "Bianchi", 1200, vendite=5000)

    stampa_impiegato(i1)
    stampa_impiegato(i2)
    
    