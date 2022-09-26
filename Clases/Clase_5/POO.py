# Clase
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    def hablar(self):
        pass
    
    def jugar(self, objeto):
        print(f"El {Animal} esta jugando con ", objeto)


class Perro(Animal):
    # Atributos de clase == global
    
    def __init__(self, nombre, raza,especie, edad):
        #Atributos de instancia == locales
        self.nombre = nombre
        self.raza = raza
        super().__init__(especie, edad)
    
    def jugar(self, objeto):
        print("El perro esta jugando con ", objeto)

    def saludar(self):
        print(f"{self.nombre} dio la pata")

class Gato(Animal):
    # Atributos de clase == global
    
    def __init__(self, nombre, raza,especie, edad):
        #Atributos de instancia == locales
        self.nombre = nombre
        self.raza = raza
        super().__init__(especie, edad)
    
    def jugar(self, objeto):
        print("El gato esta jugando con ", objeto)

    def saludar(self):
        print(f"{self.nombre} ronronea")

perro_1 = Perro("Rex", "Collie", "Perro", 5)
print(perro_1.nombre)
print(perro_1.raza)
print(f"Perro_1 - > {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}")

perro_1.saludar()

perro_2 = Perro("Juana", "Labrador", "Perro", 4)
print(perro_2.nombre)
print(perro_2.raza)
print(f"Perro_2 - > {perro_2.nombre}, {perro_2.raza}")

gato_1 = Gato("Hunter", "Calle", "Gato", 1)
print(f"gato_1 - > {gato_1.nombre}, {gato_1.raza}, {gato_1.especie}, {gato_1.edad}")
gato_1.saludar()