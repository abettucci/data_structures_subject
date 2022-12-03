###### Ejercicio 2

""" Realizar una función que, dada una cadena de caracteres y un carácter como parámetros, encuentre la
cantidad máxima de ocurrencias del carácter en la cadena """

def modaCaracter(cadena, caracter):
    maximo = cadena.count(caracter)
    print('El caracter mas repetido es {} y se repite {} veces'.format(caracter,maximo))

frase = 'Welcome to w3resource.com"'

modaCaracter(frase, "e")

# que pasa si dos caracteres se repiten la misma cantidad de veces? 
# el count solo encuentra la primera letra que ocurrio mas veces, pero si hay otra letra q aparece
# la misma cantidad de veces no la va a mostrar --> puedo crear una lista de maximos tal vez

