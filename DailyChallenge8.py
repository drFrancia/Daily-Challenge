import random

# Listas de caracteres
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
signos = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"

# Función para generar la contraseña
def generar_contraseña(longitud):
    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud de la contraseña debe estar entre 8 y 16 caracteres.")

    # Crear una lista con al menos un carácter de cada tipo
    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(signos)
    ]

    # Completar el resto de la contraseña con caracteres aleatorios de todas las listas
    todos_los_caracteres = mayusculas + minusculas + signos
    while len(contraseña) < longitud:
        contraseña.append(random.choice(todos_los_caracteres))

    # Mezclar los caracteres para que no haya un patrón predecible
    random.shuffle(contraseña)

    # Convertir la lista a un string y devolverlo
    return ''.join(contraseña)

# Pedir al usuario la longitud de la contraseña
while True:
    try:
        longitud = int(input("Introduce la longitud de la contraseña (8-16 caracteres): "))
        if 8 <= longitud <= 16:
            break
        else:
            print("La longitud debe estar entre 8 y 16 caracteres. Inténtalo de nuevo.")
    except ValueError:
        print("Por favor, introduce un número válido.")

# Generar y mostrar la contraseña
contraseña = generar_contraseña(longitud)
print(f"Contraseña generada ({longitud} caracteres): {contraseña}")
