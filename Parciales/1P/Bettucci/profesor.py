from materia import *
from auxiliar import *

class Profesor:
    listaProfesores = []

    def __init__(self):
        self.legajo = input('Legajo del profesor: ')

        #Valido que se ingrese un numero
        self.legajo = verificarNumero(self.legajo)

        self.nombre = input('Nombre del profesor: ')
        self.apellido = input('Apellido del profesor: ')
        self.materias=[]

        Profesor.listaProfesores.append(self)

    def __str__(self):
        return ('''
        Legajo: {}
        Nombre: {}
        Apellido: {}
        Materias: {}
        '''.format(self.legajo, self.nombre, self.apellido, self.materias))
    
    def agregarMaterias(self):
        cantMaterias = input('Cantidad de materias dictando: ')

        #Valido que se ingrese un numero
        cantMaterias = verificarNumero(cantMaterias)

        i=0
        for i in range(cantMaterias):
            codigoMateria = input('Codigo de la materia que dicta: ')

            #Valido que se ingrese un numero
            codigoMateria = verificarNumero(codigoMateria)

            for materia in Materia.listaMaterias:
                if codigoMateria == materia.codigo:
                    self.materias.append(materia)
                
    def listarProfesores():
        for profesor in Profesor.listaProfesores:
            print(profesor)    

    def quitarProfesor(legajoIngresado):
        for profesor in Profesor.listaProfesores:
            i = Profesor.listaProfesores.index(profesor)
            if legajoIngresado == profesor.legajo:
                for materia in profesor.materias:
                    if len(materia.profesor) == 1: #si la materia que dicta el profesor tiene solo 1 profesor, entonces es el mismo y no podemos borrarlo, porque las materias no pueden quedar sin profesores
                        exit()
                    else:
                        Profesor.listaProfesores.pop(i)
    
    def verAyudantesACargo(legajoProf):
        for profesor in Profesor.listaProfesores:
            if profesor.legajo == legajoProf:
                for materias in profesor.materias:
                    print('El profesor {}, en la materia {}, tienen a los ayudantes:'.format(profesor.nombre + ' ' + profesor.apellido, materias.nombre))
                    print('\n')
                    for ayudante in materias.ayudantes:
                        print(ayudante.alumno.nombre + ' ' + ayudante.alumno.apellido)