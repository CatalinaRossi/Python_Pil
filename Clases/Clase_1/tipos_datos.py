# Str
a = "Esto es una cadena"
b = "Esto es otra cadena"

print(a, type(a))
print(b, type(b))

c = str(120.56)
print(c, type(c))

print(len(a))
print(a[0])
print(a[0:4])
print(a[-1])

# Metodos
print(a.lower())
print(a.upper())
print(len(a.split()))

# List
lista_1 = ["hola", 4, 2.5, True, [1, 2, 3, 4], ("a", "b")]
print(lista_1)
print(type(lista_1))
print(len(lista_1))
print( lista_1[2])
var_uno = lista_1[3]
print(var_uno)
print(type(var_uno))

# Metodos
print(lista_1.append("lista"))
print(lista_1)

print(lista_1.index(("a", "b")))

lista_1.insert(1, 5)
print(lista_1)

# Diccionario
usuario = {
   "nombre" : "Octavio",
   "apellido" : "Gomez",
   "edad": 38,
   "hobbies": ["Futbol", "musica"],
   "mascotas": False 
}

print(usuario)
print(usuario["edad"])
print(len(usuario))

# Metodos

print(usuario.get("hobbies"))
print(usuario.get("Puesto", "no encontrado"))
keys_usuario = list(usuario.keys())
print(type(keys_usuario))
print(usuario.get(keys_usuario[0]))

print(usuario.values())

