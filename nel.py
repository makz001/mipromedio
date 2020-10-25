
def entradas(e=None, x=None):

    if e != None:
        try:
            e = int(e)
            if e < 10 or e > 70:
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

