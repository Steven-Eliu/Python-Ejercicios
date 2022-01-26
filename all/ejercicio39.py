#Desarrollar un programa que permita la carga 
#de 10 valores ingresados y su promedio

suma = 0 
for funcion in range (10):
    valor = int(input('Ingrese sus valores: '))
    suma = suma + valor
print('La suma de los 10 valores es: ', suma)
print('El promedio de los 10 valores es: ',  float(suma/10))
