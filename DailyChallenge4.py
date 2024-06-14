# Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.

def burbuja(lista):
    n = len(lista)
    for i in range(n):
        intercambio = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio = True
        if not intercambio:
            break
    return lista

dimension = int(input("Introduce la dimensión del vector: "))

vector = [0] * dimension

for i in range(dimension):
    vector[i] = int(input(f"Introduce el número para la posición {i+1}: "))

print("Vector cargado:", vector)
burbuja(vector)
print("Vector ordenado:", vector)


