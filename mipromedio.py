# Mipromedio
# [x] comprobar que ninguna entrada sea string
# [x] comprobar que no se ingresen 0
# [x] comprobar que la suma de las ponderaciones sea igual a 100 
# [x] especificar el formato de ingreso de notas
# [x] comprobar que la nota no sea menor a 10 ni mayor a 70

def entradas(e=None, x=None):

    if e != None:
        try:
            e = int(e)
            if e == 0 or e < 10 or e > 70:
                print('formato incorrecto')
                exit()
            else:
                return e
        except Exception as e:
            print('formato incorrecto')
            exit()

    elif x != None:
        try:
            x = int(x)
            if x == 0:
                print('formato incorrecto')
                exit()
            else:
                return x
        except Exception as e:
            print('formato incorrecto')
            exit()

def ponderaciones(li):
    s = 0
    for l in li: 
        s += l
    if s == 1.0:
        pass
    else:
        print('la suma de las ponderaciones debe ser igual a 100')
        exit()

def calcular(cant_notas):
    notas = []
    ponderacion = []
    promedio = 0
    
    print('ingresa notas sin puntos ni comas')
    print('ejemplo nota: 65   ponderacion: 20')
    for i in range(cant_notas):
        n = input('nota: ')
        notas.append(entradas(n))
        p = input('ponderacion: ')
        ponderacion.append(float('0.' + str(entradas(p))))

    ponderaciones(ponderacion)

    for i in range(len(notas)):
        promedio += (notas[i] * ponderacion[i]) 
        
    print ("promedio:", promedio)

c = input('cuantas notas?: ')
calcular(entradas(x=c))
