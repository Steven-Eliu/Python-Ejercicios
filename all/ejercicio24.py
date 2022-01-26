#Se ingresan tres valores por teclado, si todos son iguales se imprime la suma
#del primero con el segundo y a este resultado se le multiplica por el tercero

num1 = int(input('Ingrese su primer numero: '))
num2 = int(input('Ingrese su segundo numero: '))
num3 = int(input('Ingrese su tercer numero: '))

if num1 == num2 == num3:
    print((num1 + num2) * num3)
else:
    print('Vuelva a intentarlo')