"""
Realizar la carga de dos nombre por teclado. Mostrar cual de los dos es mayor alfabeticamente o si son iguales
"""

from importlib import import_module

nombre1 = input('Ingrese el primer nombre: ')
nombre2 = input('Ingrese el primer nombre: ')
if nombre1 == nombre2:
    print('Ingreso dos nombre iguales')
else:
    if len(nombre1) > len(nombre2):
        print(nombre1)
    else:
        print(nombre2)
