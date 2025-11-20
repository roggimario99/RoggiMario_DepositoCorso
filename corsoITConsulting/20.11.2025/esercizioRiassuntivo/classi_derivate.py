from classe_elettrodomestico import Elettrodomestico

#         classi derivate


# ===============================
#         LAVATRICE
# ===============================
class Lavatrice(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.capacita_kg = capacita_kg
        self.giri_centrifuga = giri_centrifuga

    def stima_costo_base(self):  # override
        """
        Costo base di diagnosi con logica:
        - 50€ base
        - +20€ se capacità > 5 kg
        - +30€ se centrifuga > 1200 gpm (giri al minuto)
        """
        costo = 50
        if self.capacita_kg > 8:
            costo += 10
        if self.giri_centrifuga > 1200:
            costo += 30
        return costo


# ===============================
#         FRIGORIFERO
# ===============================
class Frigorifero(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, litri: int, ha_freezer: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.litri = litri
        self.ha_freezer = ha_freezer

    def stima_costo_base(self):  # override
        """
        Logica esempio:
        - 50€ base
        - +20€ se ha freezer
        - +10€ se volume > 300L
        """
        costo = 50
        if self.ha_freezer:
            costo += 20
        if self.litri > 300:
            costo += 10
        return costo


# ===============================
#            FORNO
# ===============================
class Forno(Elettrodomestico):
    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione: str, ha_ventilato: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.tipo_alimentazione = tipo_alimentazione  # gas / elettrico
        self.ha_ventilato = ha_ventilato

    def stima_costo_base(self):  # override
        """
        Logica esempio:
        - 50€ base
        - +15€ se ventilato
        - +20€ se elettrico (riparazioni più costose)
        """
        costo = 50
        if self.ha_ventilato:
            costo += 15
        if self.tipo_alimentazione.lower() == "elettrico":
            costo += 20
        return costo
        