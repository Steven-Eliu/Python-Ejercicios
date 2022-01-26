"""Desarrolla un programa que solicite la carga de
10 numeros e imprima la suma de los ultimos 5 valores
ingresados """
suma = 0 
for f in range(10):
    valor = int(input('Ingrese un valor: '))
    if f >= 5: 
        suma = suma + valor
print("La suma de los ultimos 5 valores ingresados es: ", suma)