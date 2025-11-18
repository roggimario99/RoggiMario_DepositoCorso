import classi as cl

#definisco unita
unita = cl.UnitaMilitare("Falco nero", 50)
cavalleria = cl.Cavalleria("Furia del nord", 100, "rosso")
artiglieria = cl.Artiglieria("Arti", 100, ["cannoni", "fucili", "archi"])
supporto_logistico = cl.Supporto_logistico("Logisti", 5)

#testo metodi
unita.muovi()
cavalleria.esplora_terreno()
artiglieria.calibra_artiglieria()
supporto_logistico.rifornisce_unita(artiglieria)