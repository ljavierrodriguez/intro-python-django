'''
for in: 
    pass

while:
    pass

continue
break

'''

for x in range(1, 11): # start = 0, stop = n + 1, step = 1
    print(x)

nombres = ['Hugo', 'Paco', 'Luis']
print("tamaño:", len(nombres))

print('Usando indice:')
for x in range(len(nombres)): # 3 => 0, 1, 2
    print(nombres[x])

print('Usando valores:')
for nombre in nombres:
    print(nombre)

nombre = "Luis Rodriguez"
for letra in nombre:
    print(letra)

for x in range(len(nombre)):
    print(nombre[x])


status = ('active', 'inactive', 'suspended', 'canceled', 'approved', 'failed', 'pendent')
for st in status:
    print(st)

for s in range(len(status)):
    print(status[s])

frutas = { "Pera", "Manzana", "Uvas", "Limon", "Fresas", "Duraznos"}
for fruta in frutas:
    print(fruta)


persona = {
    "nombre": "Luis",
    "apellido": "Rodriguez"
}

for key in persona.keys():
    if key == 'nombre':
        continue
    else:
        print(persona[key])

for value in persona.values():
    print(value)


for fruta in frutas:
    if fruta == 'Limon':
        break
    else:
        print(fruta)


x = 1
while x <= 10:
    print(x)
    x+=1

y = 0
while y < len(status):
    print(status[y])
    y+=1

s = 'active'
num = 1
while num < 5:
    print(s)
    if num == 3:
        break
    num+=1