"""Confeccionar un prgrama que permita ingresar
un valor del 1 al 10 y nos muestre la tabla de
multiplicar del mimso los primeros 12 terminos
"""

valor = int(input('Ingrese un valor entre 1 y 10: '))
for f in range(1,13):
    tabla = valor * f
    print(tabla) 