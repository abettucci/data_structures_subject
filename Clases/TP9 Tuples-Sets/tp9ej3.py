'''Teniendo en cuenta los métodos ofrecidos por un set en Python, se pueden computar estas 
operaciones utilizando los métodos (1) union, (2) intersection y (3) difference. 

Escriba una función que pueda utilizarse como un ‘calculador de conjuntos’ para estas 3 operaciones sobre conjuntos 
de enteros no negativos (!!) . La función recibirá una lista de listas, donde cada lista contendrá dos conjuntos y 
la operación que deberealizarse, entre ellos.'''

conjunto1 = {1,2,3}
conjunto2 = {3,5,7}

def unirConjuntos(conjunto1, conjunto2):
    conjuntoUnion = conjunto1.union(conjunto2)
    return conjuntoUnion

def intersectarConjuntos(conjunto1, conjunto2):
    conjuntoUnion = conjunto1.intersection(conjunto2)
    print(conjuntoUnion)

def diferenciaConjuntos(conjunto1, conjunto2):
    conjuntoUnion = conjunto1.difference(conjunto2)
    print(conjuntoUnion)

def calculadorDeConjuntos():
    corriendo = True
    while corriendo == True:

        opcionIngresada = input('''
            1. Union de conjuntos
            2. Interseccion de conjuntos
            3. Diferencia entre conjuntos
            4. Finalizar
            Ingrese que accion desea realizar: ''')

        while opcionIngresada.isnumeric() == False:
            print("\nIngrese un numero\n")
            opcionIngresada = input('Ingresar una opcion nuevamente: ')   
        opcionIngresada = int(opcionIngresada)

        if opcionIngresada == 1:
            unirConjuntos(conjunto1, conjunto2)
            opcionIngresada=input('Ingrese una nueva accion: ')

        elif opcionIngresada == 2:
            intersectarConjuntos(conjunto1, conjunto2)
            opcionIngresada=input('Ingrese una nueva accion: ')

        elif opcionIngresada == 3:
            diferenciaConjuntos(conjunto1, conjunto2)

        elif opcionIngresada == 4:
            corriendo = False

        else:
            print('\n Ingrese un numero valido \n')

calculadorDeConjuntos()