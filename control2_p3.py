#escriba un programa en python que permita el  ingreso de n palabras a una lista.
# para finalizar el ingreso debera ingresar un vacio(enter).
#finalmente, debera indicar cuantos caracteres tiene la palabra con la menor canidad de caracteres
lista=[]
while True:
    palabra=input("ingrese una palabra ")
    if palabra=="":
       break
    lista.append(palabra)
    
    if lista:
      x= min(len(palabra)
      for palabra in (lista))
    print("la menor cantidad de caracteres es", x)