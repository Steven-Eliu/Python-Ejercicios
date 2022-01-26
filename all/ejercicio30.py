'''Una planta que fabrica perfiles de hierro posee un lote de n piezas
Confeccionar un programa que pida ingresar por teclado la cantidad de 
piezas a procesar y luego ingrese la logitud de cada perfil; sabiendo
que la pieza cuya logitud este comprendida en el rango de 
1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas 
aptas que hay en el lote  '''

x = 1
cantidad = 0
n = int(input('Ingrese cuantas piezas va a procesar: '))
while x <= n:
    largo = float(input("Ingrese la medida de la pieza: "))
    if largo >= 1.20 and largo <= 1.30:
        cantidad = cantidad + 1
    x = x + 1
print('Canitdad de piezas aptas: ', cantidad)

        
