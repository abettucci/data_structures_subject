'''
Escribir un método que calcule el producto de dos números enteros positivos mediante sumas sucesivas 
en forma recursiva
'''

# def verificar(numero):
#     while numero < 0 or numero.isnumeric() is False:
#         numero = input('Ingrese un numero y que sea positivo: ')
#     numero = int(numero)

# numero1 = input('Ingrese numero: ')
# verificar(numero1)
# numero2 = input('Ingrese numero: ')
# verificar(numero2)

def multiplicar(a, b):
   if a == 0:
      return 0
   elif a == 1:
      return b
   else:
      return b + multiplicar(a-1, b)

print(multiplicar(3,5))
