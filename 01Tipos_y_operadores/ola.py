modo = int(input("elige una opción:\n1. conversión de galeones a sickels\n2. conversión de galeones a knuts\n3. conversión de sickels a knuts\n4. conversión de knuts a galeolnes, sickels y knuts (mínimo número de monedas posibles)"))
if (modo == 1):
    galeones = int(input("cuantos galeones tienes?"))
    sickels = galeones * 17
    print("tienes", sickels, "sickels")
elif (modo == 2):
    galeones = int(input("cuantos galeones tienes?"))
    knuts = galeones * 17 * 29
    print("tienes", knuts, "knuts")
elif (modo == 3):
    sickels = int(input("cuantos sickels tienes?"))
    knuts = sickels * 29
    print("tienes", knuts, "knuts")
elif (modo == 4):
    knuts = int(input("cuantos knuts tienes?"))
    galeones = knuts // 493
    sickels = (knuts // 29) % 17
    knuts = knuts % 29
    print("tienes", galeones, "galeones,", sickels, "sickels y", knuts, "knuts")
else:
    print("no has elegido un modo válido")