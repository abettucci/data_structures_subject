import matplotlib.pyplot as plt
import numpy as np


class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []
        self.alumnos = []
        self.profesores = []

    def __str__(self):
        return self.nombre

    def lista_legajos_alumnos(self):
        lista = []
        for alumno in self.alumnos:
            lista.append(alumno.legajo)
        return lista

    def lista_legajos_profesor(self):
        lista = []
        for profesor in self.profesores:
            lista.append(profesor.legajo)
        return lista

    def lista_codigo_materia(self):
        lista = []
        for materia in self.materias:
            lista.append(materia.codigo)
        return lista

    def lista_materias_x_universidad(self):
        lista = []
        for materia in self.materias:
            lista.append(str(materia))
        return lista

    def lista_profesores_x_universidad(self):
        lista = []
        for profesor in self.profesores:
            lista.append(str(profesor))
        return lista

    def lista_cantidad_x_materia(self):
        lista = []
        for materia in self.materias:
            lista.append(len(materia.lista_alumnos()))
        return lista

    def lista_cantidad_x_profesor(self):
        lista = []
        for profesor in self.profesores:
            lista.append(len(profesor.materias))
        return lista

    def grafico_alumnos_x_materia(self, universidad):
        plt.title(label="Cantidad de alumnos por materia", loc="center")
        plt.xlabel("Materias")
        plt.ylabel("Cantidad de alumnos")
        plt.bar(universidad.lista_materias_x_universidad(),
                universidad.lista_cantidad_x_materia())
        plt.show()

    def grafico_materia_x_profesor(self, universidad):
        plt.title(label="Cantidad de materias por profesor", loc="center")
        plt.xlabel("Profesor")
        plt.ylabel("Cantidad de materias")
        plt.bar(universidad.lista_profesores_x_universidad(),
                universidad.lista_cantidad_x_profesor())
        plt.show()


class Nodo():
    def __init__(self, data=None, prox=None):
        self.data = data
        self.prox = prox

    def __str__(self):
        return str(self.dato)


class Lista:
    def __init__(self):
        self.inicio = None
        self.len = 0

    def agregar_final(self, nodo: Nodo):
        if (self.len == 0):
            self.head = nodo
        else:
            nodomov = Nodo()
            nodomov = self.head
            while (nodomov.prox != None):
                nodomov = nodomov.prox
            nodomov.prox = nodo


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.materias = []

    def __str__(self):
        Datos = self.nombre + " " + self.apellido
        return Datos

    def lista_materias(self):
        lista = []
        for materia in self.materias:
            lista.append(str(materia))
        return lista


class Alumno(Persona):
    def __init__(self, universidad, nombre, apellido, legajo):
        super().__init__(nombre, apellido)
        if legajo in universidad.lista_legajos_alumnos():
            raise ValueError(f"El legajo ya existe en {universidad.nombre}")
        self.legajo = legajo
        universidad.alumnos.append(self)

    def estudia(self, materia):
        if self.creditos() + materia.creditos > 24:
            raise ValueError('El alumno excede los 24 creditos')
        self.materias.append(materia)

    def baja_materia(self, materia):
        if materia not in self.materias:
            raise ValueError(
                f'El alumno {self.nombre} no esta cursando esta materia')
        self.materias.pop(materia)

    def creditos(self):
        creditos = 0
        for mat in self.materias:
            creditos += mat.creditos
        return creditos

    def lista_profesores(self):
        lista = []
        for materia in self.materias:
            if str(materia.profesor) not in lista:
                lista.append(str(materia.profesor))
        return lista

    def ayuda(self, materia):
        if self not in materia.ayudantes:
            materia.ayudantes.append(self)

    def lista_materias_ayudante(self, universidad):
        lista = []
        for materia in universidad.materias:
            if self in materia.ayudantes:
                lista.append(str(materia))
        return lista

    def visualizar_materias_ayudante(self, universidad):
        if len(self.lista_materias_ayudante(universidad)) == 0:
            return "El alumno no es ayudante en ninguna materia"
        else:
            for materia in self.lista_materias_ayudante(universidad):
                return ('\n'.join(materia))

    def lista_materias_x_alumno(self):
        lista_materia = Lista()
        for materia in self.materias:
            nodo = Nodo(materia)
            lista_materia.agregar_final(nodo)
        return lista_materia


class Profesor(Persona):
    def __init__(self, universidad, nombre, apellido, legajo):
        super().__init__(nombre, apellido)
        if legajo in universidad.lista_legajos_profesor():
            raise ValueError(f"El legajo ya existe en {universidad.nombre}")
        self.legajo = legajo
        universidad.profesores.append(self)

    # def ensena(self, materia):
    #     if not materia.profesor:
    #         materia.profesor = self
    #         self.materias.append(materia)

    def ensena(self, materia):
        if self not in materia.profesores:
            materia.profesores.append(self)
            self.materias.append(materia)

    def lista_alumnos(self):
        lista = []
        for materia in self.materias:
            for alumno in materia.lista_alumnos():
                if alumno not in lista:
                    lista.append(alumno)
        return lista

    def baja_ensena(self, materia):
        if materia not in self.materias:
            raise ValueError(
                f'El profesor {self.nombre} no enseña esa materia')
        if len(materia.profesores) <= 1:
            raise ValueError(
                'No podes eliminar a este profesor antes de conseguir alguien que lo suplante')
        materia.profesores.remove(self)
        self.materias.remove(materia)

    def lista_ayudantes(self):
        ayudantes = []
        for materia in self.materias:
            for ayudante in materia.ayudantes:
                if str(ayudante) not in ayudantes:
                    ayudantes.append(str(ayudante))
        return ayudantes


class Materia:
    def __init__(self, universidad, codigo, nombre, creditos):
        self.nombre = nombre
        self.universidad = universidad
        self.profesores = []
        self.ayudantes = []
        self.notas = np.array([])
        if creditos <= 6 and creditos > 0:
            self.creditos = creditos
        else:
            raise ValueError('No se puede tener mas de 6 creditos')
        if codigo not in universidad.lista_codigo_materia():
            self.codigo = codigo
        else:
            raise ValueError(f"La materia ya existe en {universidad.nombre}")
        universidad.materias.append(self)

    def __str__(self):
        return self.nombre

    def lista_alumnos(self):
        lista = []
        for alumno in self.universidad.alumnos:
            if str(self) in alumno.lista_materias():
                lista.append(str(alumno))
        return lista

    def lista_profs(self):
        lista = []
        for prof in self.profesores:
            lista.append(str(prof))
        return lista