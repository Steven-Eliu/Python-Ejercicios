# Confecciona un programa que pida por teclado tres notas de un alumno, 
# Calcule el promedio e imprima alguno de estos mensajes

cal1 = int(input('Ingrese su primer calificacion: '))
cal2 = int(input('Ingrese su segunda calificacion: '))
cal3 = int(input('Ingrese su tercera calificacio: '))

promedio = (cal1 + cal2 + cal3) / 3
if promedio >= 9:
    print('Felcidades aprobaste')
else:
    if promedio >= 4:
        print('Regular')
    else:
        print('Ya pinchaste chavo')
