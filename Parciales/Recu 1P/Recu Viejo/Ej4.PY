
lista1 = [1,2,3]
lista2 = [1,2,3,4,5]

lista3 = ['A','B','%']
lista4 = ['B','C','%','4','#','A']

def guardarListaEnArchivo(lista):
    with open("Modelo recu2.csv",'w') as csvlista:
        for elemento in range(len(lista)):
            csvlista.write(str(lista[elemento]))

def evaluarListaContenidaEnOtra(lista1,lista2):
    if len(lista1) > len(lista2):
        if all(elemento in lista1 for elemento in lista2): #ver si lista1 CONTIENE a lista2
            print('La lista {} contiene a la lista {}'.format(lista1,lista2))
            guardarListaEnArchivo(lista1)
        else:
            print('Las listas no comparten todos los elementos')
    else:
        if all(elemento in lista2 for elemento in lista1): #ver si lista2 CONTIENE a lista1
            print('La lista {} contiene a la lista {}'.format(lista2,lista1))
            guardarListaEnArchivo(lista2)
        else:
            print('Las listas no comparten todos los elementos')

evaluarListaContenidaEnOtra(lista1,lista2)
evaluarListaContenidaEnOtra(lista3,lista4)