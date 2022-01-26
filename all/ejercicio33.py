"""En una empresa trabajan n empleados cuyos sueldo oscilan entre $100 y $500, realizar un 
programa que lea los sueldos que cobra cada empleado e informe cuantos empleados cobran entre 
$ 100 y $ 300 y cuantos cobran mas de $300 ademas el programa debera informar el importe que 
gasta la empresa en sueldos al personal """

suma_sueldo = 0
bajos = 0 
altos = 0 
empleados = int(input('Cuantos empleados quiere calcular: '))
x = 1 
while x <= empleados:
    sueldo = int(input('Ingrese su sueldo: '))
    suma_sueldo = sueldo + suma_sueldo
    if sueldo <= 300:
        bajos = bajos + 1
    else:
        altos = altos + 1
    x = x + 1    

print('Numero de empleados con sueldos entre 100 y 300: ', bajos)
print('Numero de empeados que cobran mas de 300: ', altos )
print('Importe que se gasta en salarios' , suma_sueldo)
