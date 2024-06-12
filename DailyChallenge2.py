# Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

num = int(input("Ingrese un numero: "))
print(f"La tabla del {num} es: ")
for i in range(11):
    print(f"{num} * {i} = {i * num}")