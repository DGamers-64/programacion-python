def recortarDecimales(num, decimales):
    num = str(num)
    numNuevo = ''
    esDecimal = False
    for i in num:
        numNuevo += i
        if (i == '.'):
            esDecimal = True
            continue
        
        if (esDecimal):
            decimales -= 1
            if(decimales == 0):
                break
    return numNuevo

print(recortarDecimales(3.143281, 3))