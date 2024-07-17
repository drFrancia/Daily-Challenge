#Eliminar duplicados: Implementa una función que elimine los elementos duplicados de una lista de 10 enteros.
def eliminar_duplicados(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7]
lista_sin_duplicados = eliminar_duplicados(lista_con_duplicados)
print("Lista original:", lista_con_duplicados)
print("Lista sin duplicados:", lista_sin_duplicados)
