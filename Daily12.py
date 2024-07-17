#Figura y Círculo: Crea una clase base Figura con un método imprimir y una clase derivada Círculo que extienda Figura y sobreescriba el método imprimir.

class Figura:
    def imprimir(self):
        print("Soy una figura")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def imprimir(self):
        print(f"Soy un círculo con radio {self.radio}")

figura = Figura()
figura.imprimir()


circulo = Circulo(5)
circulo.imprimir()
