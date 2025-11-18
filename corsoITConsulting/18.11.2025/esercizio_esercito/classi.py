#---------------------------------------------------------------
# Classe base
#---------------------------------------------------------------

class UnitaMilitare:
    
    def __init__(self, nome: str, numero_soldati: int):  #attributi: nome dell'unità (str), numero di soldati nell'unità (int)
        self.nome = nome
        self.numero_soldati = numero_soldati
        
    def muovi(self):
        print(f"L'unità {self.nome} è ora in movimento!")
        
    def attacca(self):
        print(f"L'unità {self.nome} va all'attacco!")
        
    def ritira(self):
        print(f"L'unità {self.nome} va in ritirata!")    
        
#---------------------------------------------------------------
# Classi derivate
#---------------------------------------------------------------
        
class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        self.tipo = "fanteria"
        
    def costruisci_trincea(self):
        print(f"La fanteria {self.nome} costruisce una tricea")
        
class Artiglieria(UnitaMilitare):
    def __init__(self, nome: str, numero_soldati: int, pezzi: list): #attributi: pezzi è una lista con i pezzi di artiglieria
        super().__init__(nome, numero_soldati)
        self.pezzi = pezzi
        self.tipo = "artiglieria"
        
    def calibra_artiglieria(self):
        print(f"L'artiglieria {self.nome} calibra i suoi:{", ".join(self.pezzi)}.")
        
class Cavalleria(UnitaMilitare):
    def __init__(self, nome: str, numero_soldati: int, colore_cavallo: str): #attributi: pezzi è una lista con i pezzi di artiglieria
        super().__init__(nome, numero_soldati)
        self.colore_cavallo = colore_cavallo
        self.tipo = "cavalleria"
        
    def esplora_terreno(self):
        print(f"La cavalleria {self.nome} esplora nuovo terreno con i suoi cavalli colore {self.colore_cavallo}.")
        
class Supporto_logistico(UnitaMilitare):
    def __init__(self, nome: str, numero_soldati: int): #attributi: pezzi è una lista con i pezzi di artiglieria
        super().__init__(nome, numero_soldati)
        self.tipo = "supporto logistico"
        
    def rifornisce_unita(self, unita): #unita è un oggetto di una delle classi derivate di Unitamilitare
        print(f"Il supporto logistico {self.nome} rifornisce l'unità {unita.tipo} {unita.nome}.")        

#---------------------------------------------------------------
# Classi che erida tutte le altre
#---------------------------------------------------------------        
class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, Supporto_logistico):
    def __init__(self, unita_registrate: dict = {}):
        self.unita_registrate = unita_registrate
        
    def registra_unità(self, unita):
        if unita.tipo in self.unita_registrate.keys():
            self.unita_registrate[unita.tipo] += 1 
        else:
            self.unita_registrate[unita.tipo] = 0
                
