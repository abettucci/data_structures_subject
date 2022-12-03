# from collections import deque   
# from queue import Queue

# x = '1/5/2019'
# y = '1/3/2019'
# x = x.split('/')
# y = y.split('/')

# x = int(x[0])/365 + int(x[1])/12 + int(x[2]) #dia mes año
# y = int(y[0])/365 + int(y[1])/12 + int(y[2]) #dia mes año

# print('años: ', x)
# print('años: ', y)
# print(x>y)


def transformacionFecha(fecha : str):
    return fecha.split(sep="/")
def transformacionHora(hora: str):
    return hora.split(sep=":") 
def valorNumericofechaHora(fecha, hora): 
    listaFecha=transformacionFecha(fecha)
    listaHora=transformacionHora(hora)
    retorno=listaFecha[2]
    if len(listaFecha[0])==1:
        retorno+="0"
    retorno+=listaFecha[0]
    if len(listaFecha[1])==1:
        retorno+="0"
    retorno+=listaFecha[1]
    if len(listaHora[0])==1:
        retorno+="0"
    retorno+=listaHora[0]
    if len(listaHora[1])==1:
        retorno+="0"
    retorno+=listaHora[1]
    return(retorno)


print(transformacionFecha("1/3/2019"))
print(valorNumericofechaHora("1/3/2019",'09:00:00'))