from persona import Persona
from estudiante import Estudiante

p1 = Persona("Rodrigo", "Smith", 30) # p1 es una instancia u objeto del tipo Persona
#p1.nombre = "Rodrigo"
p1.color_ojo = "red"
p1.comer()

p2 = Persona("John", "Doe", "unknow")
#p2.nombre = "Luis"
p2.comer()

e1 = Estudiante("Jane", "Doe", "Unknow", "3-2", "Medicina", "Universidad de Chile", "Medicina")
e1.comer()