# Recorrido en amplitud (BFS): Implementa un recorrido BFS para un grafo simple con 5 nodos.

from collections import deque

grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

def bfs(grafo, inicio):
    nodo_visitado = set()
    fila = deque([inicio])
    
    while fila:
        nodo = fila.popleft()
        
        if nodo not in nodo_visitado:
            nodo_visitado.add(nodo)
            print(nodo, end = " ")
            
            for vecino in grafo[nodo]:
                if vecino not in nodo_visitado:
                    fila.append(vecino)

bfs(grafo, 0)
