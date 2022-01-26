'''Se cuentas con la siguiente informacion
Las edades de 5 estudiantes del turno  mañana
Las edades de 6 estudiantes del turno tarde 
las edades de 11 estudiantes del turno noche
las edades de cada estudiante deben ingresarse por teclado
    Obtener el promedio de las edades de cada turno(tres promedios)
    Imprimir dichos promedios 
    Mostrar por pantalla un mensaje que indique cual de los tres
    turnos tienen un promendio de edades mayor'''

mañana= 0
tarde = 0 
noche = 0 

for m in range(5):
    mañana_datos = int(input("Ingrese las edades de los 5 estudiantes de la manana: "))
    mañana = mañana_datos + mañana
for m in range(6):
    tarde_datos = int(input("Ingrese las edades de los 6 estudiantes de la tarde: "))
    tarde = tarde_datos + tarde
for m in range(11):
    noche_datos = int(input("Ingrese las edades de los 11 estudiantes de la manana: "))
    noche = noche_datos + noche

mañana_promedio = mañana / 5 
tarde_promedio = tarde / 6
noche_promedio = noche / 11

print('El promedio de alumnos de la manana es: ', mañana_promedio)
print('El promedio de alumnos de la tarde es: ', tarde_promedio)
print('El promedio de alumnos de la noche es: ', noche_promedio)

if mañana_promedio > tarde_promedio and mañana_promedio > noche_promedio:
    print("El promedio de edad es mayor en la manana")
else:
    if tarde_promedio > noche_promedio:
        print("El promedio de edad es mayor en la tarde")
    else: 
        print("El promedio de edad es mayor en la noche")
