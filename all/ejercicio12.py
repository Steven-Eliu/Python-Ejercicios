#Ingresan tres notas de un alumno, si el promedio es mayor iguala siete
#mostrar un mensaje de "Aprobado"

nota1 = int(input('Ingrese su primer calificacion: ')) 
nota2 = int(input('Ingrese su segunda calificacion: '))
nota3 = int(input('Ingrese su tercera calificacion: '))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 7:
    print('Aprobado')
else:
    print('Ya fuiste chavo')