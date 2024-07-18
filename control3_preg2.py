#Crear un programa en Python que implemente una función
#“convierte_negativo(lista)”, que reciba una lista con 10
#números enteros positivos ingresados por el usuario. La función
#deberá devolver la misma lista con los números convertidos a
#negativo. En el programa principal mostrar el resultado final
#de la lista. 




def convierte_negativo(lista):
    for x in range(len(lista)):

        lista[x] = -lista[x]  


numeros = []
for i in range(10):
    num = int(input("Ingrese número positivo "))
    numeros.append(num)

convierte_negativo(numeros)

print("los numeros en negativo")
print(numeros)



