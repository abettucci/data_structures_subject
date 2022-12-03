from profesor import *
from auxiliar import *

class Materia:
    listaMaterias = []

    def __init__(self):
        self.codigo = input('Codigo de la materia: ')

        #Valido que se ingrese un numero
        self.codigo = verificarNumero(self.codigo)

        self.nombre = input('Nombre de la materia: ')
        self.creditos = input('Creditos de la materia: ')

        #Valido que se ingrese un numero
        self.creditos = verificarNumero(self.creditos)

        #Valido que sea una materia con < 6 y > 0 creditos
        while self.creditos > 6 or self.creditos < 0:
            self.creditos = verificarNumero(input('Ingrese un valor de creditos entre 0 y 6: '))

        self.profesor=[]
        self.alumnos=[]
        self.notas=[]
        self.ayudantes=[]

        Materia.listaMaterias.append(self)

    def __str__(self):
        return ('''
        Codigo: {}
        Nombre: {}
        Creditos: {}
        Profesores: {}
        Alumnos: {}
        Notas: {}
        Ayudantes: {}
        '''.format(self.codigo, self.nombre, self.creditos, self.profesor, self.alumnos, self.notas, self.ayudantes))

    def listarMaterias():
        for materia in Materia.listaMaterias:
            print(materia)    


                    