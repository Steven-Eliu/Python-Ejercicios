#Se carga una fecha (dia, mes y a­ño), por teclado. Mostrar un mensaje si corresponde al primer
#trimestre del año 

dia = int(input('Ingrese dia : '))
mes = int(input('Ingrese mes : '))
año = int(input('Ingrese año : '))

if mes == 1 or mes == 2 or mes == 3:
    print('Corresponde al primer trimestre')
else: 
    print('fin')

