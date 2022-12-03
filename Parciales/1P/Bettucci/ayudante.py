from alumno import Alumno

class Ayudante(Alumno):
    listaAyudantes = []

    def __init__(self,alumno):
        self.materiasAyudante = []
        self.alumno = alumno
        Ayudante.listaAyudantes.append(self)

    def __str__(self):
        return 'El alumno {} {} de legajo {}, es ayudante en la materia {}'.format(self.alumno.nombre,self.alumno.apellido,self.alumno.legajo,self.materiasAyudante)

