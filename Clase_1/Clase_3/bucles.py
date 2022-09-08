# for
# for i in "Python":
#     print(i)

# lista = [True, False, 1, 2, 3, 4, "Hola"]
# for i in lista:
#     print(i)

# lista_1 =[]
# for i in range(0, 10, 2):
#     lista_1.append(i)

# print(lista_1)

# lista_2 =[]
# for i in range(3):
#     dato_ingreso = input("Ingrse un numero: ")
#     if dato_ingreso.isnumeric():
#         lista_2.append(int(dato_ingreso))
#     else:
#         print("No es un numero")
#         break

# print(lista_2)

# while
x= 10
while x > 0:
    print(x)
    x -=  1

print('1 - Deposito\n2 - Extranccion\n3 - Transferencia\n4 - Salir')    
opcion = int(input('ingrese la opcion deseada'))

print('\n\n### Bienvenido al cajero ###\n\n')
print('### ¿A qué opción desea ingresar? ###\n\n')
while True:
    print('  1 - DEPOSITO \n')
    print('  2 - EXTRACCION \n')
    print('  3 - TRANSFERENCIA \n')
    print('  4 - SALIR \n')
    opcion = int(input('Ingrese el número de la opción deseada: '))
    
    if opcion == 1:
        x = int (input('Ingrese el monto a Depositar: '))
    elif opcion == 2:
        x = int (input('Ingrese el monto a Extraer: '))
    elif opcion == 3:
        x = int (input('Ingrese el monto a Transferir: '))
    elif opcion == 4:
        print('Usted Salió')
        break
    else:
        print("El número ingresado no es una opcion")
