class Persona:
    def __init__(self, nome: str, eta: int):
        # attributi "privati" con name mangling
        self.__nome = nome
        self.__eta = eta
        
    def presentazione(self):
        # ritorna una frase base con nome ed età
        return f"{self.__nome} ha {self.__eta} anni."
        
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_eta(self):
        return self.__eta      
    
    def set_eta(self, eta):
        self.__eta = eta
        
class Studente(Persona):
    def __init__(self, nome: str, eta: int, voti: list[float]):
        super().__init__(nome, eta)
        # attributo pubblico per semplicità; contiene la lista dei voti
        self.voti = voti

    def __calcola_media(self):
        # protezione contro divisione per zero se la lista dei voti è vuota
        if not self.voti:
            return 0.0
        return sum(self.voti) / len(self.voti)
        
    def presentazione(self):
        # riusa la presentazione base e aggiunge la media
        base = super().presentazione()
        media = self.__calcola_media()
        # formatta la media con 2 decimali
        return f"Lo studente {base} La sua media è: {media:.2f}."
        
class Professore(Persona):
    def __init__(self, nome: str, eta: int, materia: str):
        super().__init__(nome, eta)
        # materia insegnata dal professore
        self.materia = materia
        
    def presentazione(self):
        base = super().presentazione()
        # aggiunge la materia alla frase base
        return f"Il professore {base} Insegna {self.materia}."
        

        