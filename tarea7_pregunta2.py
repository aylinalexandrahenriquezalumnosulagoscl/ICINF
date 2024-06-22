#Crear un programa en Python que permita ingresar, mediante un bucle,
#N palabras en una lista. Para finalizar, deberá ingresar un vacío (Enter).
#Al finalizar, deberá mostrar cuantos caracteres de letras “A” o “a” tiene
#cada palabra de la lista.
lista=[]

def contarletra(palabra):
    contador = 0
    for letra in palabra:
        if letra == "A" or letra == "a":
            contador += 1
    return contador


while True:
    n=input("ingrese una palabra (enter para finalizar)")
    if n=="":
        break
    lista.append(n)
    for palabra in lista:
      cantidad = contarletra(palabra)
      print(f"Palabra {palabra} tiene {cantidad} letras A o a")
    
