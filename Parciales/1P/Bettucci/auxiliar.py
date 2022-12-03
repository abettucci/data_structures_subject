def verificarNumero(Numero):
    while Numero.isnumeric() == False:
        Numero = input('Se debe ingresar un numero: ')
    return int(Numero)

