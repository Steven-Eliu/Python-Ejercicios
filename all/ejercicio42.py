"""Confeccionar un programa que lea n pares de datos,
cada par de datos corresponde a la medida de la
base y la altura de un triangulo
 """

triangulos = int(input('Cuantos triangulos calculara: '))
cantidad = 0
for t in range(triangulos):
    base = int(input('Ingrese el valor de la base: '))
    altura = int(input('Ingrese el valor de la altura: '))
    area = base * altura / 2
    print('El area del triangulo es: ', area)
    if area > 12:
        cantidad = cantidad + 1
print('La cantidad de triangulos con superficie < 12 son: ', cantidad)