//Escribir un programa que pida al usuario dos números y los sume. ¡Pero esta vez hazlo en C++! :)
#include<iostream>

using namespace std;

int main(){
    int num1, num2, result;
    cout << "Suma de numeros kk" << endl;
    cout << "Ingrese el primer numero: " << endl;
    cin >> num1;
    cout << "Ingrese el segundo numero: " << endl;
    cin >> num2;
    
    result = num1 + num2;

    cout << "La suma de ambos numeros es igual a: " << result << endl;
}