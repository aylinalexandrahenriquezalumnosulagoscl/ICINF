#Crear una función recursiva llamada “potencia(num, exp)”, que
#reciba un número (num) y un exponente (exp), y calcule su
#potencia en base al exponente. NO DEBE UTILIZAR FUNCIONES
#PREDEFINIDAS DE PYTHON O LIBRERÍAS para calcular la potencia.






def potencia(num, exp):
    if exp == 1:
        return num
    elif exp == 0:
        return 1
    else:
        return num * potencia(num, exp - 1)

print(potencia(2, 4))  
