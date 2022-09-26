class Personaje:
    #atributos globales
    vida = 100

    # constructor
    def __init__(self, esVillano):
        self.esVillano = esVillano
    
    def recibir_golpe(self, danio):
        self.vida -= danio
    
    def dar_golpe(self):
        pass
    
    def get_vida(self):
        return self.vida

class Terrorista(Personaje):
    
    def __init__(self, nombre):
        self.nombre = nombre
        super().__init__(True)
    def dar_golpe(self, Antiterrorista):
        Antiterrorista.vida -= 10


class Antiterrorista(Personaje):
    def __init__(self, nombre):
        self.nombre = nombre
        super().__init__(False)

    def dar_golpe(self, Terrorista):
        Terrorista.vida -= 10


terrorista_1 = Terrorista("Bin Laden")
print(f"Este terrorista es {terrorista_1.nombre} y tiene {terrorista_1.vida} de vida")
terrorista_1.recibir_golpe(10)
print(terrorista_1.get_vida())

antiterrorista_1 = Antiterrorista("Mary")
antiterrorista_1.dar_golpe(terrorista_1)
print(terrorista_1.get_vida())

terrorista_1.dar_golpe(antiterrorista_1)
print(f"Despues de una bomba {antiterrorista_1.nombre} se quedó con {antiterrorista_1.get_vida()} de vida")