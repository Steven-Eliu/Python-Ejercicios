#Si el sueldo es inferior a 500 y su antiguedad es igual o superiror a 10 años, otorgarle un aumento del 20% mostrar el sueldo a pagar
#Si el sueldo es inferior a 500 y su antiguedad es menor a 10 años, otorgarle un amuento de 5%
#Si el sueldo es mayor o igual a 500 mostrar el sueldo en patalla sin cambios

sueldo = int(input('Ingrese su sueldo: '))
antiguedad = int(input('Ingrese su antiguedad en años: '))

if sueldo < 500 and antiguedad >= 10:
    print(sueldo * 1.20)
else:
    if sueldo < 500:
        print(sueldo * 1.05)
    else:
            print(sueldo)
            