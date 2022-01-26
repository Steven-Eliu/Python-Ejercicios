#Realizar un programa que lea cuatro valores numericos e informar su suma y promedio

from typing import Counter


num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
num3 = int(input('Ingrese el tercer numero: '))
num4 = int(input('Ingrese el cuarto numero: '))

suma = num1 + num2 + num3 + num4
prom = (suma)/4

print('La suma es: ')
print(suma)
print('El promedio de los numeros es: ')
print(prom)
