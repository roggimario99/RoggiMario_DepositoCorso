from classi_derivate import Auto
from classi_derivate import Furgone
from classi_derivate import Motocicletta

class GestoreParcoVeicoli():
    def __init__(self, veicoli: list = []):
        self._veicoli = veicoli
        
    def aggiungi_veicolo(self, veicolo):
        self._veicoli.append(veicolo)
        
    def rimuovi_veicolo(self, marca, modello):
        for v in self._veicoli:
            if v.marca == marca and v.modello == modello:
                self._veicoli.remove(v)
        
    def lista_veicoli(self):
        print("### Lista veicoli ###")
        for v in self._veicoli:
            print(v)
