#Crear una función recursiva llamada “potencia(num, exp)”, que
#reciba un número (num) y un exponente (exp), y calcule su
#potencia en base al exponente. NO DEBE UTILIZAR FUNCIONES
#PREDEFINIDAS DE PYTHON O LIBRERÍAS para calcular la potencia.







def potencia(num, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    else:
        resultado = num
        for x in range(1, exp):
            resultado = resultado * num
        return resultado

print(potencia(2, 3))  
