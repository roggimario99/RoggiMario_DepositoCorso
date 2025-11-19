class Veicolo:
    def __init__(self, marca: str, modello: str, anno: int, accensione: bool = False):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione =  accensione
        
    def __str__(self):
        def __str__(self):
            return (f"Marca: {self._marca}, Modello: {self._modello}, Anno: {self._anno}, Accensione: {'Accesa' if self._accensione else 'Spenta'}")
        
    def accendi(self):
        if not self._accensione:
            self._accensione = True
            print("Macchina accesa!")
        else:
            print("Macchina già accesa!")
            
    def  spengi(self):
        if self._accensione:
            self._accensione = False
            print("Macchina spenta!")
        else:
            print("Macchina già spenta!")           
        
    
#v = Veicolo("citroen", "C1", 2017, False)

