# Crear un programa en Python que permita ingresa al usuario, mediante
#un bucle, de 10 números en una lista. Finalmente, recorrer los elementos
#de la lista en el orden inverso de cómo fueron ingresados.
#Por ejemplo, si el usuario ingresa los números 23, 40, 11, 13, 7, 18, 32,
#338, 13, 35, al finalizar, el programa mostrará 35, 13, 38, 32, 18, 7, 13,
#11, 40, 23.

lista=[]
for x in range (10):
    x=int(input("ingrese un numero: "))
    lista.append(x)
    
print(lista, "lista normal")
lista=lista[::-1]
print(lista, "lista inversa")