### Ejercicio 7

''' Utilice funciones built-in del caso, dada una lista de nombres haga una lista 
donde almacena la cantidad de letras a o A que hay en cada nombre de la lista

Ejemplo1:

listaCiudad=["Mendoza", "Salta", "Catamarca", "Iguazu","Bariloche", "Pumamarca","Armenia"]
listas=[1,2,4,1,1,3,2]
'''
listaCiudad=["Mendoza", "Salta", "Catamarca", "Iguazu","Bariloche", "Pumamarca","Armenia"]
listas=[]

for i in range(len(listaCiudad)):
    if 'a' in listaCiudad[i]:
        print(listaCiudad[i])
        print('cantidad de a: ',listaCiudad[i].count('a'))
        if 'A' in listaCiudad[i]:
            print('cantidad de A: ',listaCiudad[i].count('A'))
            listas.append(listaCiudad[i].count('A')+listaCiudad[i].count('a'))
        else:
            listas.append(listaCiudad[i].count('a'))
    elif 'A' in listaCiudad[i]:
        print(listaCiudad[i])
        print('cantidad de A: ',listaCiudad[i].count('A'))
        listas.append(listaCiudad[i].count('A'))

