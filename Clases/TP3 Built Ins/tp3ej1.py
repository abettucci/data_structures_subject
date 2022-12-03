### Ejercicio 1

''' Realizar una función anónima que tenga como parámetro z y regrese el valor de z al 
cuadrado. Realice el llamado de la función anónima correctamente y visualice la respuesta 
obtenida

Ejemplo:

z=2
visualizara: 2 elevado al cuadrado es 4

'''
z=2

#def elevadorAlCuadrado(z):
#    z = z**2
#    return z
#print(z,' elevado al 2 es ',elevadorAlCuadrado(z))

cuadrado = lambda z: z**2
print(z,' elevado al 2 es ',cuadrado(2))






