'''Realiza la carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el nombre de la persona con 
mayor altura '''

# Persona 1

print('Ingrese los datos de la primera persona')
nombre1 = input('Ingrese el nombre: ')
edad1 = int(input('Ingrese la edad: '))
altura1 = float(input('Ingrese la altura (Ej: 1.72): '))
print('Ingrese los datos de la segunda persona: ')
nombre2 = input('Ingrese el nombre: ')
edad2 = int(input('Ingrese la edad: '))
altura2 = float(input('Ingrese la altura (Ej: 1.72): '))

if altura1 > altura2:
    print(nombre1)
else:
    print(nombre2)
