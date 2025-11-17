class Ristorante:
    def __init__(self,nome,tipo_cucina, menù,aperto = False):   #costruttore
        self.nome =nome                                #nome del ristorantte (str)
        self.tipo_cucina = tipo_cucina                 #tipo di cucina (str)
        self.aperto = aperto                           #True se il ristorante è aperto, false se è chiuso. E' false di defoult. (bool)
        self.menù = menù                               #dizionario col menù {piatto : prezzo} (dict)
        
    def descrivi_ristorante(self): #descrizione del ristorante
        print(f"Il ristorante si chiama {self.nome} e fa cucina {self.tipo_cucina}.")
        
    def stato_apertura(self): #stampa se il ristorante è aperto o chiuso
        match self.aperto:  
            case True:
                print("Il ristorante è aperto!")
            case False:
                print("Il ristorante è chiuso!")
                
    def apri_ristorante(self): #setta apertura a True se non lo è già e printa lo stato di apertura del rist
        match self.aperto:  
            case True:
                print("Il ristorante è già aperto!")
            case False:
                self.aperto = True
                print("Il ristorante è ora aperto!")
                
    def chiudi_ristorante(self): #setta apertura a False se non lo è già e printa lo stato di apertura del rist
        match self.aperto:  
            case True:
                self.aperto = False
                print("Il ristorante è ora chiuso!")
            case False:
                print("Il ristorante è già chiuso!")
                
    def aggiungi_al_menù(self, piatto, prezzo):
        self.menù[piatto] = prezzo
        
    def togli_dal_menù(self, piatto):
        if piatto in self.menù.keys():     
            self.menù.pop(piatto)
        
    def stampa_menù(self):
        print("### Menù ###")
        for k, v in self.menù.items():
            print(f"{k}: {v}$")
            
menu = {"gyoza" : 7, "sahimi salmone" : 15, "uramaki mango" : 10}            
myRist = Ristorante("Suki Sushi", "Giapponese", menu, True)   

#test metodi
print("\nmetodo descrivi_ristorante")
myRist.descrivi_ristorante()

print("\nmetodo stato_apertura")
myRist.stato_apertura()

print("\napri_ristorante")
myRist.apri_ristorante()

print("\nmetodo chiudi_ristorante")
myRist.chiudi_ristorante()


myRist.aggiungi_al_menù("carbonara",15)


myRist.togli_dal_menù("uramaki mango")

print("\nmetodo stampa_menù")
myRist.stampa_menù()
        