from materia import *
from auxiliar import *

class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        listaMaterias = []
        temp = self.head
        while(temp):
            listaMaterias.append(temp.data),
            temp = temp.next
        return listaMaterias

class Alumno:
    listaAlumnos = []

    def __init__(self):
        self.legajo = input('Legajo alumno: ')

        #Valido que se ingrese un numero
        self.legajo = verificarNumero(self.legajo)

        self.nombre = input('Nombre alumno: ')
        self.apellido = input('Apellido alumno: ')
        self.materias = []
        self.ayudantia = []
        self.notas = []

        Alumno.listaAlumnos.append(self)

    def __str__(self):
        return '''
        Legajo: {}
        Nombre: {}
        Apellido: {}
        Materias: {}
        Materias ayudante: {}
        Notas: {}
        '''.format(self.legajo, self.nombre, self.apellido, self.materias, self.ayudantia, self.notas)

    def listarAlumnos():
        for alumno in Alumno.listaAlumnos:
            print(alumno)
    
    def agregarMaterias(self):
        llist = LinkedList()
        cantMaterias = input('Cantidad de materias cursando: ')
        #Valido que se ingrese un numero
        cantMaterias = verificarNumero(cantMaterias)
        i=0
        for i in range(cantMaterias):
            sumaCreditos = 0
            codigoMateria = input('Codigo de la materia: ')

            #Valido que se ingrese un numero
            codigoMateria = verificarNumero(codigoMateria)

            #Calculo la cantidad de creditos actual que lleva el alumno con las materias que cursa
            for materias in self.materias:
                sumaCreditos += materias.creditos
        
            for materia in Materia.listaMaterias:
                if codigoMateria == materia.codigo:
                    #Valido que no se superen los 24 creditos por alumno al agregar la materia nueva
                    if sumaCreditos + materia.creditos > 24:
                        print('No se puede agregar la materia {}, ya que se excede de 24 creditos'.format(materia.nombre))
                    else:
                        llist.push(materia)
        
        llist.printList()

        #self.materias = llist.printList()

    # def agregarAyudantias(self):
    #     cantMateriasAyudante = input('Cantidad de materias de ayudante: ')

    #     #Valido que se ingrese un numero
    #     cantMateriasAyudante = verificarNumero(cantMateriasAyudante)

    #     i=0
    #     for i in range(cantMateriasAyudante):
    #         codigoMateria = input('Codigo materia en la que es ayudante: ')

    #         #Valido que se ingrese un numero
    #         codigoMateria = verificarNumero(codigoMateria)

    #         for materia in Materia.listaMaterias:
    #             if codigoMateria == materia.codigo:
    #                 self.ayudantia.append(materia)
    
    def quitarAlumno(legajoIngresado):
        for alumno in Alumno.listaAlumnos:
            i = Alumno.listaAlumnos.index(alumno)
            if legajoIngresado == alumno.legajo:
                Alumno.listaAlumnos.pop(i)

    def agregarNotas(legajoIngresado):
        for alumno in Alumno.listaAlumnos:
            if legajoIngresado == alumno.legajo:
                for materia in alumno.materias:
                    print('Materia a calificar: {}'.format(materia.nombre))
                    notaMateria = input('Nota de la materia: ')

                    #Valido que se ingrese un numero
                    notaMateria = verificarNumero(notaMateria)

                    alumno.notas.append([materia.codigo,notaMateria])

    def promedioNotas(legajoIngresado):
        promedioAlumno = []
        i=0
        for alumno in Alumno.listaAlumnos:
            if legajoIngresado == alumno.legajo:
                for materias in alumno.notas:
                    promedioAlumno.append(alumno.notas[i][1])
                    i += 1
                break

        if len(promedioAlumno) == 0:
            exit()
        else:        
            print('Promedio del alumno {}: '.format(alumno.nombre + ' ' + alumno.apellido),sum(promedioAlumno)/len(promedioAlumno))

    def promedioAlumnadoEnMateria(codigoMateria): #deberia ir en Materia esta funcion pero me tira referencia circular de importacion
        promedioNotasDeMateria = []
        for materias in Materia.listaMaterias:
            if materias.codigo == codigoMateria:
                for alumno in Alumno.listaAlumnos:
                    i=0
                    for i in range(len(alumno.notas)):
                        if alumno.notas[i][0] == materias.codigo:
                            promedioNotasDeMateria.append(alumno.notas[i][1])
                        i += 1
                break
        if len(promedioNotasDeMateria) == 0:
            exit()
        else:
            print('Promedio del alumnado de la materia {}: '.format(materias.nombre),sum(promedioNotasDeMateria)/len(promedioNotasDeMateria))