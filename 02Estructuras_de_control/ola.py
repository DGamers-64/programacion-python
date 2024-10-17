filas = int(input("cuantas filas quieres?"))
columnas = 1
contador = filas

for i in range(1, filas+1):
    for j in range(0, contador):
        print(" ", end="")
    for n in range (0, columnas):
        print("*", end="")
    columnas += 2
    contador -= 1
    print("\n", end="")