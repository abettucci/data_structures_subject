# para el ejercicio de reemplazar caracteres podia usar replace('caracter a reemplazar', 'reemplazo')
 
## Una forma del ej 7

import string
frase2 = 'abc'
cadena=[]
for i in string.string.ascii_lowercase:
    repeticiones = frase2.count()
    if repeticiones != 0:
        frase_nueva = i + hex(repeticiones).replace('0x',"")
        cadena.append(frase_nueva)
cadena = ''.join(cadena)
cadena= ''.join(reversed(cadena))
print(cadena)

## una forma del ej 8

frase ='abbc'
lista = []
for char in frase:
        if char not in lista:
                lista.append(char)          
lista.reverse()
for char in lista:
    texto = str(char(frase.count(char)))[2:] + char
print(texto)

