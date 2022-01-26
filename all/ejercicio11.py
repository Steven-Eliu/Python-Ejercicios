#Realizar un programa que solicite la carga por teclado de dos numeros,
#si el primero es mayor al segundo informar su suma y diferencia, 
# en caso contrario informar el producto y la division del primero respecto al segundo 

num1 = int(input('Ingrese su primer numero: '))
num2 = int(input('Ingrese su segunfo numero: '))

if num1 > num2:
    suma = num1 + num2
    resta = num1 - num2
    print('El primer numero es mayor, por lo tanto la suma de los valores es: ', suma, 'y la resta es: ', resta)
else: 
    pro = num1 * num2
    div = num1 / num2
    print('El segundo numero es mayor, por lo tanto la multiplicacione de los valores es: ', pro, 'y la division es: ', div)