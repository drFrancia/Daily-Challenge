#Clase de Punto 2D: Crea una clase Punto2D con atributos x & y, y un método para imprimir sus coordenadas.
class Punto2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir_coordenadas(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

punto = Punto2D(3, 4)
punto.imprimir_coordenadas()
