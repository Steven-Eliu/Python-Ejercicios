#Se cargan por teclado tres numeros dstinto:s. Mostrar por pantalla el mayor de ellos.

num_1 = int(input('Ingrese su primer numero: '))
num_2 = int(input('Ingrese su segundo numero: '))
num_3 = int(input('Ingrese su tercer numero: '))

if num_1 > num_2:
    if num_1 > num_3:
        print(num_1)
    else:
        print(num_3)
else:
    if num_2 > num_3:
        print(num_2)
    else:
        print(num_3)