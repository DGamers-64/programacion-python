def esBisiesto(año):
    if (año % 4 != 0 or año % 400 != 0 and año % 100 == 0):
        return False
    else:
        return True
    
añoMin = int(input("dime un año"))
añoMax = int(input("dime otro año mayor a este"))
if(añoMin > añoMax):
    print("años invalidos")
    exit()
print("hola")