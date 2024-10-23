import random

def comprobar(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    match p1:
        case "tijeras":
            match p2:
                case "tijeras":
                    resultado = "tie"
                case "piedra":
                    resultado = "cpu"
                case "papel":
                    resultado = "p1"
        case "piedra":
            match p2:
                case "tijeras":
                    resultado = "p1"
                case "piedra":
                    resultado = "tie"
                case "papel":
                    resultado = "cpu"
        case "papel":
            match p2:
                case "tijeras":
                    resultado = "cpu"
                case "piedra":
                    resultado = "p1"
                case "papel":
                    resultado = "tie"
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
    print("CPU:      ", p2, "\n")
    resultado = comprobar(p1, p2)
    match (resultado):
        case 'p1':
            print("Has ganado", "\n")
        case 'cpu':
            print("Ha ganado la CPU", "\n")
        case 'tie':
            print("Has empatado", "\n")
    jugar = input("¿Quieres seguir jugando? (s/n) ")
    print()
    return jugar

jugar = "s"
while (jugar == "s"):
    jugar = juego()
print("¡Gracias por jugar!")

