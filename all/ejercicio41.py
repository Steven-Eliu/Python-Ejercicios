"""Codificar un programa que lea n numeros enteros
y calcule la cantidad de valores mayores o iguales
a 1000"""
mayores = 0 
valores = int(input('Ingrese cuantos valores quiere calcular: '))

for numeros in range (valores):
    carga = int(input('Ingrese el valor: '))
    if carga >= 1000:
        mayores = mayores + 1 
print('La cantidad de valores ingresados mayores o iguales a 1000 son: ', mayores)