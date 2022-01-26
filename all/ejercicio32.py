#Se ingresa un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas

x = 1
suma = 0 
personas = int(input('Ingrese el numero de personas que quiere contar: '))

while x <= personas:
    alturas = float(input('Ingrese su altura: '))
    suma = suma + alturas
    x = x + 1
promedio = suma / personas
print('El promedio de altura es: ', promedio)