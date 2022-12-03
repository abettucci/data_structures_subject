class Alumno():
    listaAlumnos = []
    def __init__(self,nombre,edad,DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        for alumnos in Alumno.listaAlumnos:     
            if self.DNI == alumnos.DNI:
                raise ValueError ("DNI repetido")
        Alumno.listaAlumnos.append(self)
    def __str__(self):
        return 'El alumno {} tiene {} años y su DNI es {}'.format(self.nombre,self.edad,self.DNI)
    def mostrarAlumnos():
        for alumno in Alumno.listaAlumnos:
            print(alumno) 

try:
    juan = Alumno('juan',23,40505050)
    Alumno.mostrarAlumnos()
    carlos = Alumno('carlos',23,40505050)
except ValueError as e:
    print(e)
