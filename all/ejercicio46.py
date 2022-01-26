"""Realizar un programa que lea los lados de n
triangulos, e informar:
"""
equilatero = 0
isosceles = 0 
escaleno = 0

ntrian = int(input('Ingrese el numero de triangulos a calcular: '))
for nrtrian in range(ntrian):
    lado_1 = int(input('Ingrese la primer medida: '))
    lado_2 = int(input('Ingrese la segunda medida: '))
    lado_3 = int(input('Ingrese la tercer medida: '))
    if lado_1 == lado_2 and lado_1 == lado_3:
        equilatero = equilatero + 1
        print('Es equilatero')
    else:
        if lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
            isosceles = isosceles + 1
            print('Es isosceles')
        else: 
            if lado_1 != lado_2 and lado_1 != lado_3:
                escaleno = escaleno + 1
                print('Es escaleno')

print("La cantidad de triangulos equilateros ingresados son: ", equilatero)
print("La cantidad de triangulos isosceles ingresados son: ", isosceles)
print("La cantidad de triangulos escaleno ingresados son: ", escaleno)
