'''
Escribir un método recursivo que permita sumar los dígitos de un número entero positivo. 
Por ejemplo, si el número es 1234 la respuesta será 10
'''

def sum_digit(n):
    if n > 0:
        return sum_digit(n // 10) + n % 10
    else:
        return 0

print(sum_digit(1234))

# 1234 // 10 --> me redondea 123,4 a 123 y la cuenta de n%10 me deja de  resto el 4
# luego hace otra vez 123 // 10 = 12,3 y me redondea a 12 y la cuenta de n%10 me deja de resto el 3
# luego hace otra vez 12 // 10 = 1,2 y me redondea a 1 y la cuenta de n%10 me deja de resto el 2
# luego hace 1 // 10 = 0,1 y me redondea a 0 y la cuenta de n%10 me deja de resto el 1
# por ultimo queda 0 como parametro de sum_digit(n//10), como es "n" = 0 devuelve 0 y el 
# resultado queda como la suma de los restos: 4 + 3 + 2+ + 1
