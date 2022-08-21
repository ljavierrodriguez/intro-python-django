class Persona:
    nombre = None
    apellido = None
    edad = None
    color_ojo = None

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def comer(self):
        print(self.nombre +  ": Estoy Comiendo...")