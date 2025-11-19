import classi_scuola as scuola

# istanze di esempio
p = scuola.Persona("Mario", 26)
stud = scuola.Studente("Antonio", 17, [3, 5, 6, 9])
# qui si deve creare un'istanza di Professore (non Studente)
prof = scuola.Professore("Lucci", 43, "Inglese")

print(p.presentazione())
print(stud.presentazione())
print(prof.presentazione())