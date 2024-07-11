def separar(lista):
    pares = []
    impares = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
   
    
    return pares, impares


numeros = [6, 5, 2, 1, 7]
pares, impares = separar(numeros)

print("Números pares:", pares)
print("Números impares:", impares)
