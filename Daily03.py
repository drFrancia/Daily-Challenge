# Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

def dfs(grafo, inicio, nodovisitado = None):
    if nodovisitado is None:
        nodovisitado = set()
    
    nodovisitado.add(inicio)
    print(inicio, end = " ")
    
    for vecino in grafo[inicio]:
        if vecino not in nodovisitado:
            dfs(grafo, vecino, nodovisitado)

dfs(grafo, 0)
