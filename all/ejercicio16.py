#Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el numero es positivo negativo
# o nulo

numero = int(input('Ingrese un numero: '))

if numero == 0:
    print('Ingreso valor nulo')
else:
    if numero > 0:
        print('Ingreso un valor positvo')
    else:
        print('Ingreso un valor negativo')