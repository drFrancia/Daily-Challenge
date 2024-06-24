#include <iostream>
using namespace std;

void cambioVariable(int a, int b) {
    int aux = a;
    a = b;
    b = aux;
}

void ordenamientoBurbuja(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                cambioVariable(arr[j], arr[j+1]);
            }
        }
    }
}

void imprimir_vector(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    cout << "Array original: " << endl;
    imprimir_vector(arr, n);
    
    ordenamientoBurbuja(arr, n);
    
    cout << "Array ordenado: " << endl;
    imprimir_vector(arr, n);
    
    return 0;
}
