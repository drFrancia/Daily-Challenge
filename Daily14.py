class Animal:
    def hacerSonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Perro(Animal):
    def hacerSonido(self):
        return "Guau"

"""animal = Animal()
print(animal.hacerSonido())  
"""
perro = Perro()
print(perro.hacerSonido())
