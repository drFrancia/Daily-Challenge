# Recursión Factorial: Implementa una función recursiva para calcular el factorial de un número pequeño (por ejemplo, 5).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un numero: "))
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
