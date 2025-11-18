#Classe base

class Animale:
    def __init__(self, nome):
        self.nome = nome
        
    def parla(self):
        print(f"{self.nome} fa suono generico.")
        
#Classe derivata (eriditata da animale)

class Cane(Animale):
    
    def parla(self):
        print(f"{self.nome} abbaia.")
        
animale_gen = Animale("Animale generico")
cane = Cane("Fido")

animale_gen.parla()
cane.parla()

class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    def mostra_informazioni(self):
        print(f"marca: {self.marca}, modello: {self.modello}.")

class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
        
    def mostra_dotazioni(self):
        print(f"dotazioni speciali: {", ".join(self.dotazioni)}")

### ereditarietà multipla
        
class AutomobileSportiva(Veicolo, DotazioniSpeciali):

    def __init__(self, marca, modello, dotazioni, cavalli):

        Veicolo.__init__(self, marca, modello)  

        # Alternativa a super per l'ereditarietà multipla

        DotazioniSpeciali.__init__(self, dotazioni)

        self.cavalli = cavalli


    def mostra_informazioni(self):

        super().mostra_informazioni()  

        # Chiamiamo il metodo della prima superclasse

        print(f"Potenza: {self.cavalli} CV")

        super().mostra_dotazioni()  

        # Possiamo chiamare metodi di entrambe le superclassi
        
""" veicolo = Veicolo("Citroen","c1")
veicolo.mostra_dotazioni()

dot = DotazioniSpeciali(["radio", "navigatore", "pizza"])
dot.mostra_dotazioni() """

auto = AutomobileSportiva("Citroen","c1",["radio", "navigatore", "pizza"], 100)
auto.mostra_informazioni()


auto_sportiva = AutomobileSportiva("Ferrari", "F8", ["ABS", "Controllo trazione", "Airbag laterali"], 720)
auto_sportiva.mostra_informazioni()