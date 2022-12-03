### Ejercicio 5

'''Utilice funciones built-in del caso, para crear una nueva lista aañadiendo la palabra 
Hola a cada uno delos nombres de las personas que están en una lista dada 

Ejemplo 1:

Listanombre=["Ninfa","Nicolas","Juan","Pedro"]
Listasaludo=["Hola Ninfa","Hola Nicolas","Hola Juan","Hola Pedro"]
'''

# def prepend(List, str):
#     str += '{0}'
#     List = ((map(str.format, List)))
#     return List
   
# # Driver function
# Listanombre = ['Ninfa','Nicolas','Juan','Pedro']
# str = 'Hola '
# print(prepend(Listanombre, str))

def add_to_beginning(lista, start='Hola '):
    return start + lista

lista = ['Ninfa','Nicolas','Juan','Pedro']

result = list(map(add_to_beginning, lista)) #el map me crea esa "tuplas" de nombre-hola
print(result) #el map es printeable si lo convierto en list