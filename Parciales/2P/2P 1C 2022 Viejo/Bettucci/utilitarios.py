from claseVentas import *
from datetime import datetime

def verificarFormatoID(IDinput):
    IDnumeric = IDinput.split('-')
    for numero in range(len(IDnumeric)):
        IDnumeric[numero] = IDnumeric[numero].strip()
    if len(IDnumeric) != 3:
        IDnuevo = input('Ingrese un codigo con longitud valida (xxx-xx-xxxx): ')
        verificarFormatoID(IDnuevo)
    for numero in IDnumeric:
        if numero.isnumeric() == False:
            IDnuevo = input('Ingrese un codigo numerico: ')
            verificarFormatoID(IDnuevo)
    if len(IDnumeric[0]) != 3 or len(IDnumeric[1]) != 2 or len(IDnumeric[2]) !=4:
        IDnuevo = input('Ingrese un codigo con longitud valida (xxx-xx-xxxx): ')
        verificarFormatoID(IDnuevo)

def convertirFechayHoraANumero(fechayhora):
    sumafechayhoraNumerica = 0
    fechaFormateada = datetime.strptime(fechayhora,"%m/%d/%Y %H:%M")
    sumafechayhoraNumerica += int(fechaFormateada.year*365)
    sumafechayhoraNumerica += int(fechaFormateada.month*365/12)
    sumafechayhoraNumerica += int(fechaFormateada.day)
    sumafechayhoraNumerica += int(fechaFormateada.hour*60*60)
    sumafechayhoraNumerica += int(fechaFormateada.minute*60)
    sumafechayhoraNumerica += int(fechaFormateada.second)
    return sumafechayhoraNumerica

def chequearFormatoFecha(fecha):
    fechaFormateada = fecha.split('/')
    for i in range(len(fechaFormateada)):
        if fechaFormateada[i].isnumeric() == False:
            print('Error')
            break
        else:
            if len(fechaFormateada[0]) > 2 or int(fechaFormateada[0]) not in range(0,13):
                print('Error dia')
            if len(fechaFormateada[1]) > 2 or int(fechaFormateada[1]) not in range(0,13):
                print('Error mes')  
            if len(fechaFormateada[2]) != 4 or int(fechaFormateada[2]) > 2022:
                print('Error año')

def chequearFormatoHora(hora):
    horaFormateada = hora.split(':')
    for i in range(len(horaFormateada)):
        if horaFormateada[i].isnumeric() == False:
            print('Error formato')
            break
    if len(horaFormateada[0]) > 2 or int(horaFormateada[0])>23:
            print('Error horas')
    elif len(horaFormateada[1]) > 2 or int(horaFormateada[1])>60:
            print('Error minutos')  
    elif len(horaFormateada[2]) > 2 or int(horaFormateada[2])>60:
            print('Error segundos')

# print(convertirFechayHoraANumero('01/03/2019 09:09:09'))