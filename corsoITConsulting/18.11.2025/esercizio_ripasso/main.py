from libro import Libro
from libro import Libreria

libro1 = Libro("Lo gjggy", "pippo", 5565656)
libro2 = Libro("yhgugygy", "Antonio", 5567774)
libro3 = Libro("Il gyygu", "Pluto", 5095656)

print(libro1)
libro1.descrizione()

libreria = Libreria()

libreria.aggiungi_libro(libro1)
libreria.aggiungi_libro(libro2)
libreria.aggiungi_libro(libro3)

libreria.mostra_catalogo()