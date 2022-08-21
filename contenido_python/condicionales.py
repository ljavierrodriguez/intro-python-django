import random
""" 
Condicionales:

# if simple
if condicion:
    sentences


# if  else => (opcional)
if condicion: # True
    sentences
else:
    sentences

# if anidados o nested if
if condicion:
    sentences
elif condicion:
    sentences
elif condicion:
    sentences
else: #(opcional)
    sentences

"""
""" 
Operaciones Comparativas:

Igual (==)
Diferente de (!=)
Mayor que (>)
Menor que (<)
Mayor o Igual que (>=)
Menor o Igual que (<=)

"""
a = 5
b = 10
c = 7

if a > b: # True
    print(a)


if a > b: # True
    print(a)
else: # False
    print(b)


if a > b and a > c:
    print("Mayor:", a)
elif b > c:
    print("Mayor:", b)
else:
    print("Mayor:", c)


error = None
if error is not None:
    print("Hay Errores")

nombre = None
if not nombre:
    print("Debe ingresar nombre")

if nombre == "":
    print("Debe ingresar nombre")

a = 7
b = 4
c = 5
d = 9

if a > b and a > c and a > d: # que todas las condiciones deben ser verdaderas
    print("El mayor es A")
elif b > c and b > d:
    print("El mayor es B")
elif c > d:
    print("El mayor es C")
else: 
    print("El mayor es D")


status = ('active', 'inactive', 'suspended', 'canceled', 'pendent')

status_capturado = status[random.randint(0, 4)]

if status_capturado == "canceled" or status_capturado == "suspended":
    print(status_capturado)
    print("color: danger")
else:
    print("color: success")



a = 7
b = 4
c = 15
d = 9
#   True.     True.     False 
if a > b and a > c or a > d:
    print("Verdadero") # True
else:
    print("Falso")