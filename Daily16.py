import math

class FormaGeometrica:
    def calcular_area(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

    def calcular_perimetro(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases")

class Rectangulo(FormaGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio * self.radio

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

rectangulo = Rectangulo(ancho = 4, alto = 5)
circulo = Circulo(radio = 3)

print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")

print(f"Área del círculo: {circulo.calcular_area()}")
print(f"Perímetro del círculo: {circulo.calcular_perimetro()}")
