"""
Realiza un programa que permita cargar dos listas de 15 valores cada una. 
Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor
(mensajes'Lista 1 mayor', Lista 2 mayor' 'Listas iguales')
Tener en cuanta que puede habler dos o mas estructuras repetitivas en un algoritmo
"""


acum_1 = 0
acum_2 = 0
x = 1

while x <= 15:
    lista_1 = int(input("Ingresa valores a la lista 1: "))
    acum_1 = acum_1 + lista_1
    x = x + 1
x = 1    

while x <= 15:
    lista_2 = int(input("Ingresa valores a la lista 2: "))
    acum_2 = acum_2 + lista_2
    x = x + 1  
    
if acum_1 == acum_2:
    print('Listas iguales')
else:
    if acum_1 > acum_2:
        print('Lista 1 mayor')
    else:
        print('Lista 2 mayor')
