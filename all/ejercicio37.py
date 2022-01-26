"""Desarrollar un programa que permita cargar n numero enteros y luego nos infome cuantos valores fueron
pares y cuantos impares."""

pares = 0 
impares = 0
x = 1
n = int(input('Ingrese la cantidad de numeros: '))

while x <= n:
    numero = int(input('Ingrese sus numeros: '))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    x = x + 1
print('Pares: ', pares)
print('Impares: ', impares)