# Comentario Linea Simple

""" 
Comentario de Multiples
Lineas
"""

#Tipos de Datos
'''
String
Integer
Float
Boolean
None

'''
# Tipo de Estructuras
'''

Lists
Tuples
Sets

Dict

'''

nombre_completo1 = "Luis Rodriguez" # str
nombre_completo2 = 'Luis Rodriguez' # str
nombre_completo3 =  '''        


''' # str

nombre_completo4 = """ Nombre Aqui """ # str


edad = 40 # int
edad2 = 13 # int

grades = 15.45 # float

deg = -10.5 # float

single = False # bool

flag = True # bool

# Operadores Logicos (and, or, y not)
""" 

True and True = True
True and False = False
False and False = False

True or True = True
True or False = True
False or False = False


not True and not True = False
not True and not False = False
not False and not False = True

not True or not True = False
not True or not False = True
not False or not False = True

"""

users = None


# Lists
nombres = ['Hugo', 'Paco', 'Luis'] # read and write
print(nombres[2])
nombres.append('Rodrigo')
print(nombres)
# Tuples
status = ('active', 'inactive', 'suspended', 'canceled', 'pendent') # only read
print(status[2])
# status.append('Lowed') # Error / Failed

# Sets
frutas = { "Pera", "Manzanas", "Uvas", "Sandia", "Fresas", "Pera" } # read and write # no tiene indices
frutas.remove('Pera')
frutas.add("Limon")
print(frutas) 


# Dicts
# variable = { "indice": "valor", "indice": "valor" }
persona = {
    "nombre": "Rodrigo",
    "apellido": "Concha",
    "edad": 35,
    "is_active": False
}

print(persona["nombre"]) # Rodrigo
persona["single"] = False # Creando un nuevo indice y valor en el diccionario
#print(persona["college"]) # Error KeyError

print(dir(persona)) # Devuelve todos los metodos de ese tipo de dato


persona2 = persona.copy()
print(persona2.get('nombre'))
print(persona2)
persona2.update({ "gender": "male"})
print(persona2)