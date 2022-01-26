#Se ingresan por teclado tres numero, sio todos lo valroes ingresados son menores a 10
#imprimir en pantalla la leyenda "todos los numeros son menores a 10"

num1 = int(input('Ingrese su primer numero: '))
num2 = int(input('Ingrese su segundo numero: '))
num3 = int(input('Ingrese su tercer numero: '))

if num1 and num2 and num3 < 10:
    print('Todos los numeros son menores a 10')
else: 
    print('Vuelva a intentarlo')