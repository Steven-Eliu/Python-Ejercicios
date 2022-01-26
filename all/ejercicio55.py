'''Realizar la carga de enteros por teclado
Preguntar despues que ingresa el valor si desea cargar otro valor 
debiendo el operador ingresar la cadena 'si' o 'no' por teclado.
Mostrar la suma de valores ingresados
'''
# Se definen para guardar los valores de la suma 
suma = 0 
opcion = 'si'

while opcion == 'si':
    valor = int(input('Ingrese un valor: '))
    suma = suma + valor
    opcion = input("Desea cargar otro valor (si/no)? ")
print('La suma de los valore ingresados: ', suma)

