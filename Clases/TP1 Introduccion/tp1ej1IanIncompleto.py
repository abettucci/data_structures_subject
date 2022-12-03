'''
Realizar un programa que permita Implementar un sistema que procese los datos de las personas quedesean 
tramitar su registro de conducción en una localidad del interior del país.De cada persona interesada en 
realizar el trámite se guardará la siguiente información en una lista delistas:▪ DNI: 8 dígitos, no existen 
DNI repetidos▪ Código del empleado que procesó el trámite: formado 3letras mayúsculas y 2numeros, en ese orden
▪ Tipo de licencia: PAR (particular), PRO (profesional)▪ Numero de tramite: 
generado automáticamente usando DNI + codigoempleado + código del tipo delicencia. No pueden haber Numero de 
tramites repetidosUna vez que el interesado da el examen, se guarda:▪ Nota del examen teórico (10 a 100)
▪ Nota del examen práctico (10 a 100)Para la aprobación del registro el aspirante debe haber obtenido un 
promedio entre las notas teóricas yprácticas no menor a 70.Este sistema al inicio debe mostrar un Menú 
presentando las siguientes opciones:1. Registro2. Examen3. Verificación4. SalirEl programa termina si se 
selecciona la opción 4 del menú.Para resolver las otras opciones elegidas, deberá hacerlo a través de funciones. 
(Una función a su vezpuede llamar a otras)La opción (1) Registro consiste en dar de alta a un usuario. 
Para ello se pide el DNI, código del empleado ytipo de licencia. Se genera el número de trámite, y se almacena 
en una lista (revisando que no estérepetido)La opción (2) Examen consiste en validar que el interesado esté 
registrado previamente y, si lo está, seguardan las notas de los exámenes teórico y práctico. Las notas son 
números enteros entre 10 y 100. Paravalidar si está registrado, el usuario del sistema deberá elegir 
(mediante un segundo menú) si quiere validarpor DNI (opción A) o validar por número de trámite (opción B)
La opción (3) Verificación consiste en validar que el interesado esté registrado previamente y, si lo está,
determinar si obtuvo o no el registro de conducción. Para validar si está registrado, el usuario del 
sistema deberá elegir (mediante un segundo menú) si quiere validar por DNI (opción A) o validar por número 
detrámite (opción B)
'''

from statistics import mean

corriendo = 1

def verificar_codigo_empleado(codigo):
    try:
        letras = codigo[:3].upper()
        try:
            numeros = int(codigo[3:])
        except ValueError:
            return False
        for letra in letras:
            if ord(letra) < ord("A") or ord(letra) > ord("Z"):
                return False
        return True
    except ValueError:
        return False
    
def generar_registro(matriz):
    dni = 0
    codigo_empleado = ''
    tipo_licencia = ''
    lista_DNI = generar_lista(matriz,0)

    while len(str(dni)) != 8:
        try:
            dni = int(input("Ingrese el DNI: "))
            if dni in lista_DNI:
                print("Este DNI ya esta registrado")
                dni = 0
            else:
                lista_DNI.append(dni)
        except ValueError:
            print("El DNI debe ser un numero")
    while verificar_codigo_empleado(codigo_empleado) == False:
        codigo_empleado = input("Ingrese un codigo de empleado valido: ")
    while tipo_licencia != "PAR" and tipo_licencia != "PRO":
        tipo_licencia = input("Ingrese un tipo de licencia (PAR, PRO): ").upper()
    nro_tramite = str(dni) + codigo_empleado + tipo_licencia

    matriz.append([dni, codigo_empleado, tipo_licencia, nro_tramite, 0, 0, 0])

def cargar_datos(matriz, buscar, pos):
    teorico = 0
    practico = 0
    while teorico <10 or teorico>100:
        try:
            practico = int(input("Ingrese la nota del practico: "))
        except ValueError:
            print("Ingrese un numero entero: ")
        for alumno in matriz:
            if alumno[pos] == buscar:
                alumno[4] = teorico
                alumno[5] = practico
                alumno[6] = mean(teorico + practico)
                break

def cargar_examen():
    algo = '' #aca me falta este codigo



def aprueba(matriz, buscar, pos):
    for alumno in matriz:
        if alumno[pos] == buscar:
            if alumno[6] >= 70:
                return "Examen aprobado"
            else:
                return "Examen desaprobado"

def generar_lista(matriz, pos):
    lista = []
    for usuario in matriz:
        lista.append(usuario[pos])
    return lista

def menu(): #no se si va
    opcion = '' #no se si va
    ej = 0 #no se si va
    matriz = [] #no se si va
    lista = []
    while opcion != "A" and opcion != "B":
        opcion = input("A. Buscar por DNI\nB.Buscar por tramite\nIngrese por quiere")
    if opcion == "A":
        lista = generar_lista(matriz,0)
        try:
            buscar = int(input("Ingrese el DNI: "))
        except ValueError:
            print("Ingrese un valor valido")
            return
        if buscar not in lista:
            print("No esta registrado")
            return
        if ej: #si es 1 es V
            cargar_datos(matriz, buscar,0)
        else:
            print(aprueba(matriz,buscar,0))
    elif opcion == "B":
        lista = generar_lista(matriz,3)
        buscar = input("Ingrese el nro de tramite: ")
        if buscar not in lista:
            print("No esta registrado")
            return
        if ej:
            cargar_datos(matriz,buscar,3)
        else:
            print(aprueba(matriz,buscar,3))

usuarios = []

while corriendo == 1:
    opcion = 0
    while opcion < 1 or opcion > 4:
        try:
            opcion = int(input("1. Registro\n2. Examen\n3. Verificacion\n4. Salir\n Ingrese opcion: "))
        except ValueError:
            print("Por favor ingresar uno de los numeros indicados")
    if opcion == 1: #cargando datos
        generar_registro(usuarios)
    elif opcion == 2: #examen
        cargar_examen(usuarios,1)
    elif opcion == 3: #validador
        cargar_examen(usuarios,1)
    elif opcion == 4:
        corriendo = 0
    
for linea in usuarios:
    print(linea)