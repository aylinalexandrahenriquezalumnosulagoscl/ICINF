#Crear un programa en Python que permita al usuario ingresar N palabras en una lista. Para
#finalizar, debe ingresar una palabra vacía (enter). Finalmente, mostrar la cantidad de vocales y
#consonantes de cada palabra.
def vocales_consonantes(palabra):
  vocales= "aeiouAEIOU"
  consonantes= "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
  num_vocales = sum(1 for letra in palabra if letra in vocales)
  num_consonantes = sum(1 for letra in palabra if letra in consonantes)
  return num_vocales, num_consonantes
lista=[]
vocales_consonante=input("ingrese palabra(enter para finalizar):")
lista.append(vocales_consonante)

while vocales_consonante != "":
      vocales_consonante=input("ingrese palabra(enter para finalizar):")
      lista.append(vocales_consonante)
      print(lista)
      print("cantidad de vocales y consonantes")
      for palabra in lista:
       vocales, consonantes = vocales_consonantes(palabra)
       print(f"{palabra}: Vocales - {vocales}, Consonantes - {consonantes}")
       print(lista)
