"""Se realiza la carga de 10 valores enteros por teclado
La cantidad de valores ingresados negativos
La cantidad de valores ingresados positivos
La cantidad de multiplos de 15 
El valor acumulado de los numeros ingresados que son pares
"""
positivos = 0
negativos = 0
quince = 0
pares = 0


for numero in range (10):
    numeros = int(input("Ingrese 10 valores: "))
    if numeros > 0:
        positivos = positivos + 1
    else:
        if numeros < 0:
            negativos = negativos + 1
    if numeros % 15 == 0: 
        quince = quince + 1
    if numeros % 2 == 0:
        pares = pares + numeros

print('La cantidad de numeros positivos son: ', positivos )
print('La cantidad de numeros negativos son: ', negativos )
print('La cantidad de numeros multiplos de quince son: ', quince )
print('El valor acumulado de los numero pares es : ', pares )




