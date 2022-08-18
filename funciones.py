""" 
Funciones

def nombre_funcion():
    pass

"""
import libs

def saludo():
    print("Hola Mundo 1")

def retornando_valor():
    saludo() # Hola Mundo 1
    return "Hola Mundo 2"

#saludo()

texto = retornando_valor()
print(texto) # Hola Mundo 2
# print(retornando_valor()) # Hola Mundo Hola Mundo

def operaciones(operacion, a, b):
    return operacion(a, b)

total = libs.suma(10, 10)
print(total) # 20

print(operaciones(libs.suma, 10, 15))
print(operaciones(libs.resta, 19, 30))
print(operaciones(libs.multiplicar, 100, 345))


class Persona:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "<Persona %s>" % self.name


p1 = Persona("Rodrigo")
print(p1)

p2 = Persona("Luis")
print(p2)