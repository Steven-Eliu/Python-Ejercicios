#Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora

horas = int(input('Ingrese el numero de horas trabajadas: '))
valor = int(input('Ingrese el valor por hora: '))

sueldo = (horas * valor)

print('Su sueldo es de: $', sueldo)
