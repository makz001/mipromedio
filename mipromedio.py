def calcular(cant_notas):
    suma = 0
    for i in range(cant_notas):
        n = int(input("nota: "))
        p = input("porcentaje: ")
        p = "0." + str(p)

        suma += (n * float(p)) 

    print ("promedio:", suma)

c = int(input("cuantas notas?: "))
calcular(c)
