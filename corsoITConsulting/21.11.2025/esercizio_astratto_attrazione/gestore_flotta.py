class GestoreFlotta:
    def __init__(self):
        self._veicoli = []

    def aggiungi_veicolo(self, veicolo):
        self._veicoli.append(veicolo)

    def rimuovi_veicolo(self, targa):
        for v in self._veicoli:
            if v == v._targa:
                self._veicoli.remove(v)

    def elenco_veicoli(self):
        return self._veicoli
    
    def costo_totale_manutenzione(self) -> float:
        totale = 0
        for v in self._veicoli:
            totale += v.costo_manutenzione()
        return totale
    
    def stampa_veicoli(self):
        print("### Elenco Veicoli ###")
        for v in self._veicoli:
            print(f"Targa: {v._targa}, Peso Massimo: {v._peso_massimo}, Carico Attuale: {v._carico_attuale}, Costo Manutenzione: {v.costo_manutenzione()}")