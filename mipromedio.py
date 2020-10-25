# Mipromedio
# [x] comprobar que ninguna entrada sea string
# [x] comprobar que no se ingresen 0
# [x] comprobar que la suma de las ponderaciones sea igual a 100 
# [x] especificar el formato de ingreso de notas
# [x] comprobar que la nota no sea menor a 10 ni mayor a 70

import view
import nel
from os import system

def clear():
    system('clear')


def calcular(cant_notas):
    notas = []
    ponderacion = []
    promedio = 0
    
    print('ingresa notas sin puntos ni comas')
    print('ejemplo nota: 65   ponderacion: 20')
    for i in range(cant_notas):
        n = input('nota: ')
        notas.append(nel.entradas(n))
        p = input('ponderacion: ')
        ponderacion.append(float('0.' + str(nel.entradas(p))))

    clear()
    nel.ponderaciones(ponderacion)

    for i in range(len(notas)):
        promedio += (notas[i] * ponderacion[i]) 
        
    view.results(notas, ponderacion, promedio)

def main():
    clear()
    calcular(nel.entradas(x=view.cantN()))

if __name__ == '__main__':
    main()
