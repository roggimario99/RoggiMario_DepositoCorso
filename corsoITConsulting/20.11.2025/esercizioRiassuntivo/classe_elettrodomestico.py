class Elettrodomestico:
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str):
        self.__marca = marca
        self.__modello = modello
        self.__annoacquisto = anno_acquisto   
        self.__guasto = guasto

    # ===== Getter =====

    def get_marca(self):
        return self._marca

    def Get_modello(self):
        return self._modello

    def get_annoacquisto(self):
        return self._annoacquisto

    def get_guasto(self):
        return self._guasto

    # ===== Setter =====

    def set_annoacquisto(self, valore):
        anno_corrente = 2025
        if valore > anno_corrente:
            raise ValueError("L'anno di acquisto non può essere nel futuro.")
        self._annoacquisto = valore

    def set_guasto(self, valore):

        self._guasto = valore
        
    def set_marca(self, marca):

        self._marca = marca
        
    def set_marca(self, modello):

        self._modello = modello

    # ===== Metodi =====
    def descrizione(self):

        return (f"Elettrodomestico: {self.__marca} {self.__modello}, "
                f"Acquistato nel {self.__annoacquisto}, Guasto: {self.__guasto}")

    def stima_costo_base(self):
        costo_base = 50  #costo base di diagnosi
        return costo_base