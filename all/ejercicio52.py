'''Confeccionar un programa que solicite la carga de 10 valores reales por teclado. 
Mostrar al final su suma. Definir varias lineas de comentarios indicando el nombre del programa, el programador
y la fecha de la ultima modificacion. Utilzia el caracter# para los comentarios'''

# Programa: Carga de 10 numeros reales
# Programador : Steven Eliu
# FEcha de ulrima modiciacion 13/01/22

suma = 0 
for x in range (10):
    valor = float(input('Ingrese un valor real: '))
    suma = suma + valor
print('La suma de sus valores ingresados es: ', suma)