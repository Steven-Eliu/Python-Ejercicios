"""Escribir un programa que pida ingresar cooordenanas (x, y)
que representan puntos en el plano.
Informar cuantos punros se han ingresado en el primer, segundo y
tercer y cuarto cuadrante. Al comenzar el programa se pide 
ingresar la cantidad de puntos a procesar"""

primer = 0
segundo = 0
tercer = 0
cuarto = 0 
"""
-+  ++  
--  +-
"""
puntos = int(input("Ingrese el numero de puntos a procesar: "))
for punto in range (puntos):
    x = int(input('Ingrese su coordenada x: '))
    y = int(input('Ingrese su coordenada y: '))
if x > 0 and y > 0:
    print('Pertence al primer cuadrante')
    primer = primer + 1 
else: 
    if x <  0 and y > 0:
        print('Pertenece al segundo cuadrante')
        segundo = segundo + 1
    else:
        if x < 0 and y < 0:
            print('Pertence al tercer cuadrante')
            tercer = tercer + 1
        else:
            if x > 0 and y < 0:
                cuarto = cuarto + 1
print('Cantidad de puntos ingresado en el primer cuadrante', primer)
print('Cantidad de puntos ingresado en el segundo cuadrante', segundo)
print('Cantidad de puntos ingresado en el tercer cuadrante', tercer)
print('Cantidad de puntos ingresado en el cuarto cuadrante', cuarto)



