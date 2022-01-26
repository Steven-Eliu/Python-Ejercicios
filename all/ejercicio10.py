#Realizar un programa que solicite ingresar dos numeros 
#distintos y muestre por pantalla el mayor de ellos

num1 = int(input('Ingrese su primer numero: '))
num2 = int(input('Ingrese su segundo numero: '))
if num1 > num2:
    print("El numero mayor es: ", num1)
else:
    print("El numero mayor es: ", num2)