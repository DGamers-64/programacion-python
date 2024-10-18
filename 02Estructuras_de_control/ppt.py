import random

def comprobar(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    match p1:
        case "tijeras":
            match p2:
                case "tijeras":
                    resultado = "Has empatado"
                case "piedra":
                    resultado = "Ha ganado la CPU"
                case "papel":
                    resultado = "Ha ganado el jugador 1"
        case "piedra":
            match p2:
                case "tijeras":
                    resultado = "Ha ganado el jugador 1"
                case "piedra":
                    resultado = "Has empatado"
                case "papel":
                    resultado = "Ha ganado la CPU"
        case "papel":
            match p2:
                case "tijeras":
                    resultado = "Ha ganado la CPU"
                case "piedra":
                    resultado = "Ha ganado el jugador 1"
                case "papel":
                    resultado = "Has empatado"
        case _:
            resultado = "El jugador 1 ha introducido un dato erróneo"
    return resultado

def juego():
    p1 = input("Jugador 1: ")
    p2_random = random.randrange(1,3)
    match p2_random:
        case 1:
            p2 = "Tijeras"
        case 2:
            p2 = "Piedra"
        case 3:
            p2 = "Papel"
    print("CPU:      ", p2)
    print()
    print(comprobar(p1, p2))
    print()
    jugar = input("¿Quieres seguir jugando? (s/n) ")
    print()
    return jugar

jugar = "s"
while (jugar == "s"):
    jugar = juego()
print("¡Gracias por jugar!")

