from abc import ABC, abstractmethod

class VeicolTrasposto(ABC):
    def __init__(self, targa: str, peso_massimo: int, carico_attuale: int = 0):
        self._targa = targa
        self._peso_massimo = peso_massimo
        self._carico_attuale = carico_attuale

    
    def carica(self, peso: int) -> None:
        if self._carico_attuale + peso > self._peso_massimo:
            self._carico_attuale += peso
        else:
            raise ValueError("Carico eccede il peso massimo consentito.")   
        
    def scarica(self, peso: int) -> None:
        
        self._carico_attuale = min(0, self._carico_attuale - peso)
        
    @abstractmethod
    def costo_manutenzione(self):
        pass
    
class Camion(VeicolTrasposto):
    def __init__(self, targa: str, peso_massimo: int, carico_attuale: int = 0, numero_assi: int = 2):
        super().__init__(targa, peso_massimo, carico_attuale)
        self._numero_assi = numero_assi

    def costo_manutenzione(self):
        return self._peso_massimo + (100 * self._numero_assi)
    
class Furgone(VeicolTrasposto):
    def __init__(self, targa: str, peso_massimo: int, carico_attuale: int = 0, alimentazione: str = "diesel"):
        super().__init__(targa, peso_massimo, carico_attuale)
        self._alimentazione = alimentazione

    def costo_manutenzione(self):
        if self._alimentazione.lower() == "elettrico":
            return  200
        if self._alimentazione.lower() == "diesel":
            return  150
        
class Motocarro(VeicolTrasposto):
    def __init__(self, targa: str, peso_massimo: int, carico_attuale = 0, anni_servizio: int = 0):
        super().__init__(targa, peso_massimo, carico_attuale)
        self.anni_servizio = anni_servizio
        
    def costo_manutenzione(self):
        return (50 * self.anni_servizio)
        
    

        
        
    