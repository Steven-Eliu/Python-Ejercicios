#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuantos
#tienen notas mayores o iguales a 7 y cuantos menores

x = 1
aprobados = 0
reprobados = 0
while x <= 10:
    notas = int(input('Ingrese su calificacion: '))
    if notas >= 7:
        aprobados = aprobados + 1
    else:
        reprobados = reprobados + 1 
    x = x + 1    
print('Alumnos aprobados: ', aprobados)
print('Alumnos reprobados: ', reprobados)