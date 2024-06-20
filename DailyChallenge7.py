# # Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.
import random

def playerUser():
    elecciones = ["piedra", "papel", "tijeras"]
    user_eleccion = input("Elige piedra, papel o tijeras: ").lower()
    while user_eleccion not in elecciones:
        user_eleccion = input("Entrada inválida. Elige piedra, papel o tijeras: ").lower()
    return user_eleccion

def machineChoice():
    elecciones = ["piedra", "papel", "tijeras"]
    return random.choice(elecciones)

def eval_ganador(user_eleccion, machine_eleccion):
    if user_eleccion == machine_eleccion:
        return "Empate"
    elif (user_eleccion == "piedra" and machine_eleccion == "tijeras") or \
        (user_eleccion == "papel" and machine_eleccion == "piedra") or \
        (user_eleccion == "tijeras" and machine_eleccion == "papel"):
        return "¡Ganasteeee!"
    else:
        return "¡Estas acabado, te gano una maquina kkkkk!"

def play_game():
    user_eleccion = playerUser()
    machine_eleccion = machineChoice()
    print(f"Tú elegiste: {user_eleccion}")
    print(f"La computadora eligió: {machine_eleccion}")
    result = eval_ganador(user_eleccion, machine_eleccion)
    print(result)

if __name__ == "__main__":
    play_game()
