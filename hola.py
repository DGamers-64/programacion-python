import random

lista = []
for i in range(6):
    i = []
    for j in range(7):
        i.append(random.randint(0,9))
    lista.append(i)
print(lista) 

pares = 0
impares = 0
for i in lista:
    for j in i:
        if lista[i][j] % 2 == 0:
            pares += 1
        else:
            impares += 1
print("hay", pares, "pares y hay", impares, "impares")