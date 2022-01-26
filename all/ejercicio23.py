# Se ingresan por teclado tres numero, si al menos uno de los valores ingresados, 
# Es menor a 10, imprimir en pantalla la leyenda 'Alguno de los numeros es menor a diez'

num1 = int(input('Ingrese su primer numero: '))
num2 = int(input('Ingrese su segundo numero: '))
num3 = int(input('Ingrese su tercer numero: '))

if num1 < 10  or num2 < 10 or num3 < 10:
    print('Alguno de los numeros es menor a diez')
else:
    print('Vuelva a intentarlo')
