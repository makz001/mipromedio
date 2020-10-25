def cantN():
    c = input('cantidad de notas: ')
    return c
def results(n, p, px):
    print('Resultados:\n')
    for i in range(len(n)):
        print('nota: '+str(n[i])+'   ponderacion: '
                +str(p[i]))
    print('---------------------------')
    print('promedio:', px)
