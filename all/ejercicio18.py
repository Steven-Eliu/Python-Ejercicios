"""Un postulante a un empleo, realiza un test de capacitacion
se obtuvo la siguiente informacion: cantidad total de preguntas
que se le realizaron y la cantidad de preguntas que contesto correctamente."""

#Se pide confeccionar un programa que ingrese los datos por teclado e informe el 
#nivel del mismo segun el porcentaje de respuestas correctas que han obtenido 

"""
Sabiendo que: 
    Nivel maximo porcentaje >= 90%
    Nivel medio porcentaje >= 75% y < 90%
    Nivel regular porcentaje >= 50% y < 75%
    Fuera de nivel < 50%
"""

preguntas = int(input('Ingrese el numero de preguntas: '))
correctas = int(input('Ingrese el numero de preguntas correctas: '))
porcentaje = (correctas * 100) / preguntas

if porcentaje >= 90:
    print('Nivel maximo')
else:
    if porcentaje >= 75:
        print('Nivel medio')
    else:
        if porcentaje >= 50:
            print('Nivel regular')
        else:
            print('Fuera de nivel')
    

