#include <iostream>
#include <vector>

using namespace std;

bool busquedaBinaria(const vector<int>& lista, int numero) {
    int izquierda = 0;
    int derecha = lista.size() - 1;

    while (izquierda <= derecha) {
        int medio = izquierda + (derecha - izquierda) / 2;

        if (lista[medio] == numero) {
            return true;
        }

        if (lista[medio] < numero) {
            izquierda = medio + 1;
        }
        else {
            derecha = medio - 1;
        }
    }
    return false;
}

int main() {
    int dim;
    cout << "Ingrese el tamanho del vector: " << endl;
    cin >> dim;
    vector<int> lista(dim);
    
    cout << "Ingrese el vector; ";
    for (int i = 0; i < dim; i++){
        cin >> lista[i];
    }

    int numero;
    cout << "Ingresa el número que deseas buscar: ";
    cin >> numero;

    if (busquedaBinaria(lista, numero)) {
        cout << "El número " << numero << " está en la lista." << endl;
    } else {
        cout << "El número " << numero << " no está en la lista." << endl;
    }

    return 0;
}
