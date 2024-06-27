#crear un progama en phyton que permita al usuario ingresar 10 precios de productos en dolares
#en una lista. una vez finalizado, debera invertir  los 10 precios ingresado en dolares
#a valor en pesos chilenos  (valor USD/CLP hoy: $950) modificando cada elemento de  la lista
#a su respectivo valor en pesos. finalmente, mostrar la lista resultante.                           
lista = []

for i in range(10):
    precio = float(input("Ingrese el precio en dólares: "))
    lista.append(precio)

convertir = 950
precios = []


for precio in lista:
    precio = precio * convertir
    precios.append(precio)



    print( precios)
