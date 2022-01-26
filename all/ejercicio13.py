#Se ingresa por teclado un numero positivo de uno o dos digitos,
#mostrar mensaje indicando si el numero tiene uno o dos digitos

digitos = int(input('Ingrese un numero entre 1 y 99: '))
if digitos >= 10:
    print('Tiene dos digitos')
else:
    print('Tiene un digito')