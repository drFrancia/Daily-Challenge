# Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

palabra = input("Ingrese una frase: ")
palabra_minusculas = palabra.lower()

lista_palabra = list(palabra_minusculas)
contador_vocales = 0
condicion = True

for i in range(len(lista_palabra)):
    if (lista_palabra[i] == "a"):
        contador_vocales+=1
    elif(lista_palabra[i] == "e"):
        contador_vocales += 1
    elif(lista_palabra[i] == "i"):
        contador_vocales += 1
    elif(lista_palabra[i] == "o"):
        contador_vocales += 1
    elif(lista_palabra[i] == "u"):
        contador_vocales += 1

print(f"La cantidad de vocales en esa frase es igual a: {contador_vocales}")