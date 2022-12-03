import numpy as np
from universidad import *

# El usuario selecciona la universidad que quiere y una vez creada se guarda en una lista
# Carga rapida de datos para tener algo

ITBA = Universidad("Instituto Tecnologico de Buenos Aires")
tiba = Universidad('UADE')
na = Alumno(tiba, 'Ian', "texto", 1)
ninfa = Profesor(ITBA, "Ninfa", "Esperanza", 1)
carlos = Profesor(ITBA, "Carlos", "Est", 2)
ian = Alumno(ITBA, "Ian", "Dalton", 1)
infoGeneral = Materia(ITBA, 1, "Informatica General", 6)
estructuraDatos = Materia(ITBA, 2, "Estructura de datos y programacion", 6)
a = Materia(ITBA, 3, "a", 6)
b = Materia(ITBA, 4, "b", 6)
c = Materia(ITBA, 5, "c", 6)
abril = Alumno(ITBA, "Abril", "Schafer", 2)
ian.estudia(infoGeneral)
abril.estudia(infoGeneral)
ninfa.ensena(infoGeneral)
carlos.ensena(infoGeneral)
ninfa.ensena(estructuraDatos)


universidades = [ITBA, tiba]
active = None
corriendo = True
i = 0


def ingresar_accion(i):
    selected = None
    while selected == None:
        try:
            selected = int(input("Ingrese la accion que desea realizar: "))
            if selected > i + 1 or selected < 0:
                selected = None
                print("\033[A                             \033[A")
        except ValueError:
            print("\033[A                             \033[A")
            pass
    return selected


def seleccionar(contenido, crear=0):
    if crear:
        print('0) Crear uno nuevo')
    if range(len(contenido)) == 0:
        return 0
    for i in range(len(contenido)):
        if crear:
            i += 1
            print(f'{i}) {str(contenido[i-1])}')
        else:
            print(f'{i}) {str(contenido[i])}')

    return ingresar_accion(i)


while corriendo:
    selected = None
    if not active:
        # Mostrar las opciones o crear una universidad nueva
        print("No tenes ninguna universidad seleccionada.")
        print("0) Crear una nueva")
        for i in range(len(universidades)):
            print(f"{i+1}) {str(universidades[i])}")

        selected = ingresar_accion(i)

        if selected != 0 and len(universidades) != 0:
            active = universidades[selected - 1]
        else:
            universidades.append(
                Universidad(input("Ingrese Nombre de la universidad: "))
            )
            active = universidades[len(universidades) - 1]
    opcion = 0
    while opcion < 1 or opcion > 7:  # Elegir universidad
        try:
            opcion = int(
                input(
                    """
1. Ingresar alumno
2. Ingresar profesor
3. Ingresar materia
4. Cambiar de universidad
5. Graficos
6. Salir
Ingrese su opcion: """
                )
            )
        except ValueError:
            print("Por favor ingresar uno de los numeros indicados")
    match opcion:  # Menu principal
        case 1:  # Alumnos
            opcion = 0
            selected = None
            print("No tenes ningun alumno seleccionado.")
            print("0) Crear uno nuevo")
            for i in range(len(active.alumnos)):
                print(f"{i+1}) {active.alumnos[i]}")

            if len(active.alumnos) != 0:
                selected = ingresar_accion(i)
            else:
                selected = 0
                print('No existen alumnos, se creara uno nuevo')
            if selected != 0:
                alumno = active.alumnos[selected - 1]
            else:
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                legajo = int(input("Ingrese el legajo: "))
                while legajo in active.lista_legajos_alumnos():
                    legajo = int(input("Ingrese un legajo valido: "))
                Alumno(active, nombre, apellido, legajo)
                alumno = active.alumnos[len(active.alumnos) - 1]
            while opcion < 1 or opcion > 6:
                try:
                    opcion = int(
                        input(
                            """
1) Mostrar datos del alumno
2) Mostrar profesores del alumno
3) Mostrar materias del alumno
4) Agregar alumno a una materia
5) Hacer que el alumno sea ayudante de una materia 
6) Visualizar materias en la que el alumno es ayudante
7) Salir
Ingrese su opcion: """
                        )
                    )
                except:
                    pass
            match opcion:
                case 1:  # Mostrar datos alumno
                    print(
                        f"El nombre completo del alumno es {alumno}, tiene el legajo {alumno.legajo} y esta cursando actualmente {len(alumno.materias)} materias"
                    )
                case 2:  # mostrar profesores del alumno
                    profs = ", ".join(alumno.lista_profesores())
                    print(f"El alumno {alumno} estudia bajo {profs}")
                case 3:  # Mostrar materias del alumno
                    print(alumno.lista_materias_x_alumno())

                case 4:  # Agregar alumno a una materia
                    selected = None
                    lista_habilitada = []
                    print(
                        f"Seleccionar una materia del {active} para {alumno}: ")
                    for i in range(len(active.materias)):
                        if active.materias[i] not in alumno.materias:
                            lista_habilitada.append(active.materias[i])
                    if len(lista_habilitada) != 0:
                        for i in range(len(lista_habilitada)):
                            print(f'{i}) {str(lista_habilitada[i])}')
                        while selected == None:
                            try:
                                selected = int(
                                    input("Ingrese la materia deseada: "))
                                if selected > i or selected < 0:
                                    selected = None
                                    print(
                                        "\033[A                             \033[A")
                            except ValueError:
                                print(
                                    "\033[A                             \033[A")
                        try:
                            alumno.estudia(lista_habilitada[selected])
                        except ValueError:
                            print(
                                f'El alumno esta cursando {alumno.creditos()} y la materia al valer {lista_habilitada[selected].creditos} excede el limite de 24 creditos')
                    else:
                        print(
                            f'La universidad {active} no tiene mas materias en las que {alumno.nombre} pueda estudiar')
                case 5:  # Hacer que alumno sea un ayudante
                    selected = seleccionar(active.materias)
                    materia = active.materias[selected]
                    alumno.ayuda(materia)
                    pass
                case 6:  # visualizar materias en las que es ayudante
                    print(alumno.visualizar_materias_ayudante(active))
                case 7:
                    pass

        case 2:  # Profesor
            opcion = 0
            selected = seleccionar(active.profesores, 1)
            if selected != 0:
                profesor = active.profesores[selected - 1]
            else:
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                legajo = int(input("Ingrese el legajo: "))
                while legajo in active.lista_legajos_profesor():
                    legajo = int(input("Ingrese un legajo valido: "))
                Profesor(active, nombre, apellido, legajo)
                profesor = active.profesores[len(active.profesores) - 1]
            while opcion < 1 or opcion > 7:
                try:
                    opcion = int(
                        input(
                            """
1) Mostrar datos del profesor
2) Mostrar materias del profesor
3) Mostrar alumnos del profesor
4) Ensena 
5) Dar de baja de una materia
6) Ver ayudantes
7) Salir 
Ingrese su opcion: """
                        )
                    )
                except:
                    pass
            match opcion:
                case 1:  # Mostrar datos profesor
                    print(
                        "El nombre completo del profesor es {}, tiene el legajo {}".format(
                            profesor, profesor.legajo
                        )
                    )
                case 2:  # mostrar materias del profesor
                    texto = ", ".join(profesor.lista_materias())
                    print(texto)
                case 3:  # Mostrar alumnos del profesor
                    texto = ", ".join(profesor.lista_alumnos())
                    print(texto)
                case 4:  # Agregar materia a un profesor
                    lista_habilitada = []
                    print(
                        f"Seleccionar una materia del {active} para {profesor}: ")
                    for i in range(len(active.materias)):
                        if active.materias[i] not in profesor.materias:
                            lista_habilitada.append(active.materias[i])
                    if len(lista_habilitada) != 0:
                        for i in range(len(lista_habilitada)):
                            print(f'{i}) {str(lista_habilitada[i])}')
                        while selected == None:
                            try:
                                selected = int(
                                    input("Ingrese la materia deseada: "))
                                if selected > i or selected < 0:
                                    selected = None
                                    print(
                                        "\033[A                             \033[A")
                            except ValueError:
                                print(
                                    "\033[A                             \033[A")
                        profesor.ensena(lista_habilitada[selected])
                    else:
                        print(
                            f'La universidad {active} no tiene mas materias en las que {profesor.nombre} pueda enseñar')
                case 5:  # Dar de baja en una materia
                    if len(profesor.materias) > 0:
                        selected = seleccionar(profesor.materia)
                        try:
                            profesor.baja_ensena(profesor.materias[selected])
                        except ValueError:
                            print(
                                'Si se elimina este profesor de esta materia, la materia quedara acefala')
                    else:
                        print(profesor.materias)
                case 6:  # Ver ayudantes
                    lista = profesor.lista_ayudantes()
                    print(f'El profesor {profesor.nombre} tiene {len(lista)}',
                          f'ayudantes.')
                    if len(lista) > 0:
                        texto = ', '.join(lista)
                        print(f'Ellos son: {texto}')
                case 7:
                    pass

        case 3:  # materias
            selected = seleccionar(active.materias, 1)

            if selected != 0 and len(active.materias) != 0:
                materia = active.materias[selected - 1]
            else:
                nombre = input("Ingrese el nombre: ")
                codigo = int(input("Ingrese el codigo de materia: "))
                while codigo in active.lista_codigo_materia():
                    legajo = int(input("Ingrese un legajo valido: "))
                creditos = None
                while not creditos:
                    try:
                        creditos = int(input('Seleccionar creditos (max 6) :'))
                        if creditos > 6 or creditos <= 0:
                            print('Por favor poner un numero valido')
                            creditos = None
                    except ValueError:
                        print('Por favor poner un numero valido')

                Materia(active, codigo, nombre, creditos)
                materia = active.materias[len(active.materias) - 1]
            opcion = 0
            while opcion < 1 or opcion > 7:
                try:
                    opcion = int(
                        input(
                            """
1) Mostrar datos de la materia
2) Mostrar alumnos
3) Mostrar profesores
4) Mostrar ayudantes
5) Cargar notas
6) Mostrar promedio de todos los alumnos
7) Salir 
Ingrese su opcion: """
                        )
                    )
                except:
                    pass
            match opcion:
                case 1:
                    print(
                        f"La materia {materia} con el codigo {materia.codigo} tiene un total de",
                        len(materia.lista_alumnos()),
                        f"alumnos y vale {materia.creditos} creditos",
                    )
                case 2:
                    alumnos = ", ".join(materia.lista_alumnos())
                    print(
                        f"Los alumnos de la materia {materia} son: {alumnos}")
                case 3:

                    print(
                        f"Los profesores de la materia son: {', '.join(materia.lista_profs())}")
                case 4:  # MOSTRAR AYUDANTES
                    lista = []
                    for ayudante in materia.ayudantes:
                        lista.append(str(ayudante))

                    print(
                        f'La materia {str(materia)} tiene {len(lista)} ayudantes')
                    if len(lista) != 0:
                        texto = ', '.join(lista)
                        print(f'Estos ayudantes son: {texto}')
                    pass
                case 5:
                    notas = np.array([])
                    for alumno in materia.lista_alumnos():
                        print(f'Cargar nota para {alumno}. ')
                        nota = None
                        while nota == None:
                            try:
                                nota = float(input('Nota: '))
                                print(nota)
                                if nota < 0 or nota > 10:
                                    nota = None
                            except ValueError:
                                print('Usar formato valido')
                        notas = np.append(notas, nota)
                    if len(materia.notas) == 0:
                        materia.notas = notas
                    else:
                        np.vstack((materia.notas, notas))
                case 6:
                    for i in range(len(materia.lista_alumnos())):
                        promedio = 0
                        for nota in range(len(materia.notas)):
                            promedio += float(materia.notas[nota][i])
                        promedio /= range(len(materia.notas))
                        print(f'{i}) {materia.lista_alumnos()[i]} {promedio}')

                    pass
                case 7:
                    pass

        case 4:
            active = None

        case 5:
            eleccion = int(input(
                """
1) Grafico de cantidad de alumnos por materias
2) Grafico de cantidad de materias segun el profesor
Ingrese su opcion: """))
            match eleccion:
                case 1:
                    active.grafico_alumnos_x_materia(active)

                case 2:
                    active.grafico_materia_x_profesor(active)

        case 6:
            corriendo = False