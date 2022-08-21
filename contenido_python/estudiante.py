from persona import Persona

class Estudiante(Persona):
    #nombre = None
    #apellido = None
    #edad = None
    #color_ojo = None
    curso = None
    facultad = None
    casa_de_estudio = None
    carrera = None

    def __init__(self, nombre, apellido, edad, curso, facultad, casa_de_estudio, carrera):
        super().__init__(nombre, apellido, edad)
        #self.nombre = nombre
        #self.apellido = apellido
        #self.edad = edad
        self.curso = curso
        self.facultad = facultad
        self.casa_de_estudio = casa_de_estudio
        self.carrera = carrera

    @staticmethod
    def inscribir():
        print("Inscribiendo un estudiante")

    def comer(self):
        print("Estudiante: " + self.nombre + " Estoy Comiendo...")


Estudiante.inscribir()