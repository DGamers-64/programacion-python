bloques = int(input("cuantos bloques tienes?"))
acumulador = 1
while(bloques >= acumulador):
    bloques -= acumulador
    acumulador += 1
print(acumulador-1)