"""Escribir un programa que lea 10 numero entreros 
y luego muestre cuantos valores ingresados fueron
multiplos de 3 y cuantos de 5."""

mult5 = 0
mult3 = 0

for mult in range (10):
    valores = int(input("Ingrese sus numeros: "))
    if valores % 3 == 0:
        mult3 = mult3 + 1
    if valores % 5 == 0:
        mult5 = mult5 + 1
        
print('Los valores ingresados multiplosde 3 son: ', mult3)
print('Los valores ingresados multiplosde 5 son: ',mult5)

        