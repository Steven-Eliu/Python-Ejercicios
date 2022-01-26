#Ingrese un numero positov de 3 cifras
num = int(input('Ingrese un numero positivo de hasta 3 cifras: '))

if num < 10:
    print('Tiene un digito')
else:
    if num < 100:
        print("Tiene dos digitos")
    else: 
        if num < 1000:
            print('Tiene tres digitos')
        else: 
            print('Error en la entrada de datos')