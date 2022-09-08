# Funciones basicas
# Nombre
# Argumentos/parametros
# Codigo
# Retorno

def suma(a, b):
    resultado = a + b
    return resultado

resultado_suma = suma(4, 6)
print(resultado_suma)
print(suma(4, 6))

# Funcion 2
def resta():
    resultado = 2 - 3
    return resultado
print(resta())

# Funcion 3


def saludo(cantidad_saludos):
    lista = []
    for i in range(cantidad_saludos):
        nombre = input("Ingrese su nombre: ")
        lista.append(nombre)
        print("Hola", nombre)  
    return lista

def orden(lista, sentido):
    lista.sort(reverse=sentido)
    return lista

nombres = saludo(3)
print(nombres)

print(
    orden(nombres, False)
)

# def prueba(a, b, c,):
#     print(a, b, c)
# a = 420
# b = 3
# c = 5
# prueba(b=b, c=c, a=a)