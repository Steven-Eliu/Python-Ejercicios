#Confeccionar un programa que lea por teclado tres numeros enteros 
#distintos y nos muestre el mayor 

num1 = int(input('Ingrese su numero: '))
num2 = int(input('Ingrese su numero: '))
num3 = int(input('Ingrese su numero: '))

if num1 > num2 and num1 > num3:
    print(num1)
else:
    if num2 > num3:
        print(num2)
    else: 
        print(num3)
        
