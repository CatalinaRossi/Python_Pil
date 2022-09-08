# Condicionales
a = 1
b = 2
c = 5 

if a > b:
    print("A > B")
    if a > c:
        print("a es el mayor")
else:
    print("C > A & C > B")
print("No ingreso")

if a == 3:
    print("a es igual a 3")

if a == "3":    
    print("a es igual a 3")
else:
    print("a no es igual a 3")

edad_juan = 16

if edad_juan >= 16 and edad_juan >= 18:
    print("Juan puede votar y es mayor de edad")
else:
    print("no se cumple alguna dec las condiciones")

if edad_juan >= 16 or edad_juan >= 18:
    print("Juan puede votar y es mayor de edad")
else:
    print("no se cumple alguna dec las condiciones")  

z = 5 
if z == 3:
    print("z es igual a 3")
elif z == 4:
    print("z es igual a 4")
elif z == 5:
    print("z es igual a 5")
else: 
    print("z no es igual a nada")
    
