from profesor import *
from materia import *
from alumno import *
import matplotlib.pyplot as plt
from ayudante import Ayudante

opcionIngresada= input('''
1. Cargar Profesor
2. Listar Profesores
3. Cargar Materias
4. Listar Materias
5. Cargar alumno
6. Listar alumnos
7. Ver Profesores de un Alumno
8. Ver Materias de un Profesor
9. Ver Materias de un Estudiante
10. Visualizacion Cantidad de Alumnos por Materia
11. Visualizacion Cantidad de Materias dictadas por un profesor
12. Ver Ayudantes de un profesor
13. Quitar alumnos
14. Quitar profesores
15. Obtener Promedio de una Materia
16. Cargar notas de un alumno
17. Obtener Promedio de un Alumno
18. Finalizar
Ingrese que accion desea realizar: ''')

#Valido que se ingrese un numero
opcionIngresada = verificarNumero(opcionIngresada)

while opcionIngresada != 18:

    if opcionIngresada == 1: #agregar profesor
        profesor = Profesor() #Agregamos un profesor
        Profesor.agregarMaterias(profesor)
        
        for profesor in Profesor.listaProfesores:
            for materiasUniversidad in Materia.listaMaterias:
                for materias in profesor.materias:
                    if materias.codigo == materiasUniversidad.codigo:
                        materiasUniversidad.profesor.append(profesor)

    elif opcionIngresada == 2: #listar profesores
        Profesor.listarProfesores()

    elif opcionIngresada == 3: #agregar materia
        materiaNueva = Materia() #Agregamos una materia

    elif opcionIngresada == 4: #listar materias
        Materia.listarMaterias()

    elif opcionIngresada == 5: #agregar alumno
        alumno = Alumno() #Agregamos un alumno 
        Alumno.agregarMaterias(alumno)

        for alumno in Alumno.listaAlumnos:
            for materiasUniversidad in Materia.listaMaterias:
                for materias in alumno.materias:
                    if materias.codigo == materiasUniversidad.codigo:
                        materiasUniversidad.alumnos.append(alumno)

        cantMateriasAyudante = input('Cantidad de materias de ayudante: ')
        #Valido que se ingrese un numero
        cantMateriasAyudante = verificarNumero(cantMateriasAyudante)
        i=0
        for i in range(cantMateriasAyudante):
            codigoMateria = input('Codigo materia en la que es ayudante: ')
            #Valido que se ingrese un numero
            codigoMateria = verificarNumero(codigoMateria)

            for materia in Materia.listaMaterias:
                if codigoMateria == materia.codigo:
                    ayudante = Ayudante(alumno)
                    alumno.ayudantia.append(materia)
                    ayudante.materiasAyudante.append(materia)
                    materia.ayudantes.append(ayudante)
        # Alumno.agregarAyudantias(alumno)

        # for alumno in Alumno.listaAlumnos:
        #     for materiasUniversidad in Materia.listaMaterias:
        #         for materias in alumno.ayudantia:
        #             if materias.codigo == materiasUniversidad.codigo:
        #                 materiasUniversidad.ayudantes.append(alumno)       
    
    elif opcionIngresada == 6: #listar alumnos
        Alumno.listarAlumnos()

    elif opcionIngresada == 7: #ver profesores de un alumno

        profesorIngresado = input('Ingrese el legajo del alumno: ')

        #Valido que se ingrese un numero
        profesorIngresado = verificarNumero(profesorIngresado)

        #Listar profesores de un alumno
        listaProfDelAlumno = []
        for alumno in Alumno.listaAlumnos:
            if alumno.legajo == profesorIngresado:
                for materiaAlumno in alumno.materias:
                    for profesor in Profesor.listaProfesores:
                        for materiaProfesor in profesor.materias:
                            if materiaAlumno == materiaProfesor:
                                listaProfDelAlumno.append(profesor)

        for alumno in Alumno.listaAlumnos:    
            if alumno.legajo == profesorIngresado:  
                print('\n')
                print('Profesores del alumno {} {}:'.format(alumno.nombre,alumno.apellido))
                print('\n')
        for profesor in listaProfDelAlumno:
            print(profesor.nombre + ' ' + profesor.apellido) 

    elif opcionIngresada == 8: # Ver Materias de un Profesor

        profesorIngresado = input('Legajo del profesor: ')

        #Valido que se ingrese un numero
        profesorIngresado = verificarNumero(profesorIngresado)

        #Listar materias de un profesor
        for profesor in Profesor.listaProfesores:
            if profesor.legajo == profesorIngresado:
                print('\n')
                print('Materias del profesor {} {}:'.format(profesor.nombre,profesor.apellido))
                print('\n')
                for materia in profesor.materias:
                    print(materia.nombre)

    elif opcionIngresada == 9: #Ver Materias de un Estudiante

        alumnoIngresado = input('Ingrese el legajo del alumno: ')

        #Valido que se ingrese un numero
        alumnoIngresado = verificarNumero(alumnoIngresado)

        #Listar materias de un alumno
        for alumno in Alumno.listaAlumnos:
            if alumno.legajo == alumnoIngresado:
                print('\n') 
                print('Materias del alumno {} {}:'.format(alumno.nombre,alumno.apellido))
                print('\n')
                for materia in alumno.materias:
                    print(materia.nombre) 
            

    elif opcionIngresada == 10: #Visualizacion Cantidad de Alumnos por Materia

        #cantidadAlumnosXMateria=[]
        for materias in Materia.listaMaterias:
            #cantidadAlumnosXMateria.append(len(materias.alumnos))

            plt.title(label="Cantidad de alumnos por materia", fontsize=15, color='black')
            plt.xlabel('Materias')
            plt.ylabel('Cantidad de alumnos')
            plt.bar(materias.nombre, len(materias.alumnos), color='green', width=0.5)
            plt.show()

    elif opcionIngresada == 11: #Visualizacion Cantidad de Materias dictadas por un profesor
        
        cantidadMateriasXProfesor = []
        nombresProfesores = []
        for profesores in Profesor.listaProfesores:
            cantidadMateriasXProfesor.append(len(profesores.materias))
        for profesores in Profesor.listaProfesores:
            nombresProfesores.append(profesores.nombre)
        plt.pie(cantidadMateriasXProfesor, labels=nombresProfesores, autopct='%.2f%%')
        plt.title(label='Cantidad de materias por profesor', loc='center', color='black')
        plt.show()

    elif opcionIngresada == 12: #ver ayudantes de un profesor 
        legajoProfesor = input('Legajo del profesor: ')

        #Valido que se ingrese un numero
        legajoProfesor = verificarNumero(legajoProfesor)

        Profesor.verAyudantesACargo(legajoProfesor)

    elif opcionIngresada == 13: #13. Quitar alumnos
        legajoIngresado = input('Legajo del alumno a quitar: ')

        #Valido que se ingrese un numero
        legajoIngresado = verificarNumero(legajoIngresado)

        Alumno.quitarAlumno(legajoIngresado)

    elif opcionIngresada == 14: #Quitar profesores
        legajoIngresado = input('Legajo del profesor a quitar: ')

        #Valido que se ingrese un numero
        legajoIngresado = verificarNumero(legajoIngresado)

        Profesor.quitarProfesor(legajoIngresado)

    elif opcionIngresada == 15: #calcular promedio de notas en una materia
        codigoMateriaIngresado = input('Ingrese el codigo de materia: ')

        #Valido que se ingrese un numero
        codigoMateriaIngresado = verificarNumero(codigoMateriaIngresado)

        Alumno.promedioAlumnadoEnMateria(codigoMateriaIngresado)

    elif opcionIngresada == 16: #Cargar notas de un alumno
        legajoIngresado = input('Legajo del alumno a subir sus notas: ')

        #Valido que se ingrese un numero
        legajoIngresado = verificarNumero(legajoIngresado)

        Alumno.agregarNotas(legajoIngresado)        

    elif opcionIngresada == 17: #calcular promedio del alumno
        legajoIngresado = input('Ingrese el legajo del alumno: ')

        #Valido que se ingrese un numero
        legajoIngresado = verificarNumero(legajoIngresado)

        Alumno.promedioNotas(legajoIngresado)

    opcionIngresada=input('Ingrese una nueva accion: ')

    while opcionIngresada.isnumeric() == False:
        print('Ingrese un numero de legajo valido')
        opcionIngresada=input('Intente nuevamente ingresar una opcion: ')
    opcionIngresada=int(opcionIngresada)

