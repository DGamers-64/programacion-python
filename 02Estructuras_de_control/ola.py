rows = int(input("cuantas filas quieres?"))
cols = 1



for i in range(1,rows+1):
    for j in range(0,cols):
        print("*", end="")
    cols += 2
    print("\n", end="")