// Camino mas corto: Dado un grafo pequeño con 5 nodos y 6 aristas, escribe una función que encuentre el camino más corto entre dos nodos especificados usando cualquier método que prefieras.

#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>

using namespace std;

typedef pair<int, int> Edge; // par de (nodo, altura)
const int INF = INT_MAX;

void agregarBorde(vector<vector<Edge>>& grafo, int u, int v, int w) {
    grafo[u].emplace_back(v, w);
    // grafo[v].emplace_back(u, w);  Si el grafo es dirigido
}

vector<int> dijkstra(const vector<vector<Edge>>& grafo, int origen, int destino) {
    int n = grafo.size();
    vector<int> dist(n, INF);
    vector<int> prev(n, -1); // Para reconstruir el camino
    priority_queue<Edge, vector<Edge>, greater<Edge>> pq;

    dist[origen] = 0;
    pq.emplace(0, origen);

    while (!pq.empty()) {
        int u = pq.top().second;
        pq.pop();

        if (u == destino) break;

        for (const Edge& edge : grafo[u]) {
            int v = edge.first;
            int altura = edge.second;

            if (dist[u] + altura < dist[v]) {
                dist[v] = dist[u] + altura;
                prev[v] = u;
                pq.emplace(dist[v], v);
            }
        }
    }

    // Reconstrucción del camino
    vector<int> camino;
    for (int at = destino; at != -1; at = prev[at]) {
        camino.push_back(at);
    }
    reverse(camino.begin(), camino.end());

    if (camino.size() == 1 && camino[0] != origen) {
        // si no hay camino
        return {};
    }
    return camino;
}

int main() {
    int n = 5; // Número de nodos
    vector<vector<Edge>> grafo(n);

    // Añadir aristas
    agregarBorde(grafo, 0, 1, 2);
    agregarBorde(grafo, 0, 2, 4);
    agregarBorde(grafo, 1, 2, 1);
    agregarBorde(grafo, 1, 3, 7);
    agregarBorde(grafo, 2, 4, 3);
    agregarBorde(grafo, 3, 4, 1);

    int origen = 0;
    int destino = 4;
    vector<int> camino = dijkstra(grafo, origen, destino);

    if (camino.empty()) {
        cout << "No hay camino desde " << origen << " hasta " << destino << endl;
    } else {
        cout << "El camino más corto desde " << origen << " hasta " << destino << " es: ";
        for (int nodo : camino) {
            cout << nodo << " ";
        }
        cout << endl;
    }

    return 0;
}