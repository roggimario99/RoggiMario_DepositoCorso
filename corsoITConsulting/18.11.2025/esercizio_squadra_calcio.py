#---------------------------------------------
#Classe base -- membro della squadra
#---------------------------------------------

class Membro_squadra:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def __str__(self):
        return f"nome: {self.nome}, eta: {self.eta}"
    
    def svolge_lavoro(self):
        print(f"{self.nome} fa il suo lavoro.")
    
#---------------------------------------------
#Classe base -- derivate
#---------------------------------------------
    
class Giocatore(Membro_squadra):
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        
    def __str__(self):
        base = super().__str__()
        return f"{base}, ruolo: {self.ruolo}, numero_maglia: {self.numero_maglia}"
    
    def svolge_lavoro(self):
        print(f"{self.nome} sta giocando.")
        
    gioca_partita = svolge_lavoro()    
    
class Allenatore(Membro_squadra):
    def __init__(self, nome, eta, anni_esperienza):
        super().__init__(nome, eta)
        self.anni_esperienza = anni_esperienza
        
    def __str__(self):
        base = super().__str__()
        return f"{base}, anni di esperienza: {self.anni_esperienza}"
    
    def svolge_lavoro(self):
        print(f"{self.nome} conduce gli allenamenti.")
        
    dirige_allenamento = svolge_lavoro 
    
allenatore = Allenatore("Massimo", 55, 5)
print(allenatore)
allenatore.dirige_allenamento()
allenatore.svolge_lavoro()