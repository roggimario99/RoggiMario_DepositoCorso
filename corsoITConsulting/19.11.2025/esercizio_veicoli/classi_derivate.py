from classe_Veicolo import Veicolo #import classe padre


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte ,accensione = False):
        super().__init__(marca, modello, anno, accensione)
        self._numero_porte = numero_porte
        
    def __str__(self):
        base = super().__str__()
        return f"{base}, numero_porte: {self._numero_porte}"
        
    def suona_clacson(self):
        print("La macchina sta suonando il clacson!")
        
class Furgone(Auto):
    def __init__(self, marca, modello, anno, capacita_carico, accensione=False):
        super().__init__(marca, modello, anno, accensione)
        self._capacita_carico = capacita_carico
        self.__carico = 0
        
    def __str__(self):
        base = super().__str__()
        return f"{base}, capacita_carico: {self._capacita_carico}, carico: {self.__carico}"
    
    def carica(self, carico):
        if carico + self.__carico < self._capacita_carico:
            self.__carico  += carico

    
    def scarica(self, scarico):
        self.__carico = min(0, self.__carico - scarico)
        return min(scarico, self.__carico)
    
class Motocicletta(Auto):
    def __init__(self, marca, modello, anno, tipo, accensione=False):
        super().__init__(marca, modello, anno, accensione)
        self._tipo = tipo
        
    def __str__(self):
        base = super().__str__()
        return f"{base}, tipo: {self.tipo}"
        
    def esegui_wheelie(self):
        if self._tipo.lower() == "sportivo":
            print("La moto esegue wheelie!")
        else:
            print(f"La moto non è di tipo {self.tipo} non può eseguire il wheelie!")