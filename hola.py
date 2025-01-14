grupo = ['samu', 'pedro', 'samu', 'daniel', 'daniel', 'samu']
nombre = input("nombre bro: ")
contador = 0
i = -1
acabou = False
while acabou == False:
    try:
        i = grupo.index(nombre,i+1)
        contador += 1
    except ValueError:
        print(contador)
        acabou = True