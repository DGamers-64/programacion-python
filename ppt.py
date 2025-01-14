import random

def comprobarResultado(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    match p1:
        case "tijeras":
            match p2:
                case "tijeras":
                    resultado = 3
                case "piedra":
                    resultado = 2
                case "papel":
                    resultado = 1
        case "piedra":
            match p2:
                case "tijeras":
                    resultado = 1
                case "piedra":
                    resultado = 3
                case "papel":
                    resultado = 2
        case "papel":
            match p2:
                case "tijeras":
                    resultado = 2
                case "piedra":
                    resultado = 1
                case "papel":
                    resultado = 3
        case _:
            resultado = 4
    return resultado

def p2Resultado():
    p2 = random.randrange(1,3)
    match p2:
        case 1:
            p2 = "Tijeras"
        case 2:
            p2 = "Piedra"
        case 3:
            p2 = "Papel"
    return p2

seguirJugando = "s"
while (seguirJugando == "s"):
    p1 = input("Jugador 1: ")
    p2 = p2Resultado()
    print("CPU:      ", p2, "\n")
    resultado = comprobarResultado(p1, p2)
    match (resultado):
        case 1:
            print("Has ganado", "\n")
        case 2:
            print("Ha ganado la CPU", "\n")
        case 3:
            print("Has empatado", "\n")
        case 4:
            print("El jugador 1 ha insertado una entrada no permitida\n")
    seguirJugando = input("¿Quieres seguir jugando? (s/n) ")
print("¡Gracias por jugar!")
