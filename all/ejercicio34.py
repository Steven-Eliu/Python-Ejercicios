#Realizar un programa que imprima 25 terminios de la serie 11, 22, 33, 44, etc 
x = 1
serie = 11
while x <= 25:
    print(serie)
    serie = serie + 11 
    x = x + 1

#Otra manera de resolver el problema 

x = 1 
while x <= 25:
    termino = x * 11
    print(termino)
    x = x + 1