##Piloto de eventos (Priority lista): Implementa una cola de prioridad utilizando una lista para intertar y eliminar 5 elementos.
class ColaDePrioridad:
    def __init__(self):
        self.lista = []

    def intertar(self, val):
        self.lista.append(val)
        self.lista.sort(reverse=True)  # Mantener la lista ordenada en orden descendente

    def eliminar(self):
        if not self.vacio():
            return self.lista.pop(0)  # Eliminar y retornar el elemento con la mayor prioridad
        else:
            return None

    def vacio(self):
        return len(self.lista) == 0

    def mostrar(self):
        print("Cola de prioridad:", self.lista)

# Uso de la cola de prioridad
pq = ColaDePrioridad()
elements = [20, 10, 30, 5, 15]

for val in elements:
    pq.intertar(val)

print("Después de intertarar elementos:")
pq.mostrar()

print("\nEliminando elementos de la cola de prioridad:")
for _ in range(len(elements)):
    print("Elemento eliminado:", pq.eliminar())
    pq.mostrar()
