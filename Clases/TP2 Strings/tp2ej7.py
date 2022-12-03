### Ejercicio 7 

''' Realizar una funcion que, dada una lista Palabras y dos palabras, encuentre la distancia
minima entre las palabras dadas dentro de la lista'''

Palabras = ["La", "materia", "Estructuras", "de", "Datos", "es", "genial"]
primeraPalabra = "La"
segundaPalabra = "es"
distancia = 0

for i in range(len(Palabras)):
    if primeraPalabra == Palabras[i]:
        Palabras[i] = primeraPalabra
    elif segundaPalabra == Palabras[i]:
        Palabras[i] = segundaPalabra

distancia = Palabras.index(segundaPalabra)-Palabras.index(primeraPalabra)

print("La distancia minima entre 'la' y 'es' es", distancia)