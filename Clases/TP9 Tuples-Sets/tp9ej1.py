'''Crear una clase persona sino lo ha hecho, la cual tiene como atributos el nombre (string), un id(int) y 
la edad(int), a partir de la cual se defina un Conjunto (set) de personas dentro de una función main().
Se deben crear 4 personas las cuales se deberán añadir al Conjunto. Una vez añadidas las 4 personas al
Conjunto se debe visualizar el Conjunto total usando :el método __str__ ( de la clase persona)'''

class Persona():
    def __init__(self):
        self.nombre = input('Ingrese nombre de la persona: ')
        self.id = int(input('Ingrese ID de la persona: '))
        self.edad = int(input('Ingrese edad de la persona: '))
    def __str__(self):
        return ('La persona se llama {}, con id {} y edad {} años'.format(self.nombre,self.id, self.edad))
    
def main():
    listaPersonas = set()
    N = int(input('Cantidad de personas a ingresar: '))
    for i in range(N):
        persona = listaPersonas.add(Persona())
    for personas in listaPersonas:
        print(personas)

main()