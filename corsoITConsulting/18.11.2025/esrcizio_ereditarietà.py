#Classe base

class Animale:
    def __init__(self, nome: str, eta: int):
        self.nome = nome
        self.eta = eta
        
    def __str__(self):
        return f"nome: {self.nome}, età: {self.eta}"    
        
    def parla(self):
        print(f"{self.nome} fa suono generico.")
        
#Classe derivata (eriditata da animale)

class Giraffa(Animale):
    
    def __init__(self, nome, eta, lungCollo):
        Animale.__init__(self, nome, eta) #super().__init__(nome, eta)
        self.lungCollo = lungCollo
    
    def __str__(self):
        base = super().__str__()            # ad es. "nome: Ginny, età: 6 anni"
        return f"{base}, lunghezza collo: {self.lungCollo} cm"
        
    def parla(self):
        print(f"la giraffa {self.nome} landisce.")    
        
class Pinguino(Animale):
    
    def __init__(self, nome, eta, luogo):
        Animale.__init__(self, nome, eta)
        self.luogo = luogo
        
    def parla(self):
        print(f"Il pinguino {self.nome} fa verso pinguino.")   
        
giraffa = Giraffa("Ginny", "sei anni", 70)        
print(giraffa)