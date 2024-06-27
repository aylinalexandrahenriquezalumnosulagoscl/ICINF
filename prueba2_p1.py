#crear un programa de phyton que permita al usuario ingresar N notas en
#una lista. para finalizar  debera ingresar 0. una vez finalizado, debera mostrar lo 
# siguiente: 1) cantidad de notas, 2) promedio de notas, 3) la nota minima,4) la nota maxima


lista = []

print("Ingrese las notas (ingrese 0 para finalizar):")

while True:
    nota = float(input("Ingrese una nota (0 para terminar): "))
    if nota == 0:
        break
    lista.append(nota)
    
cantidad=len(lista)

suma = 0

for nota in lista:
        suma = suma  + nota

promedio = suma / len(lista)

   
notaminima = lista[0] 
for nota in lista:
    if nota < notaminima:
        notaminima = nota

    
notamaxima = lista[0]
for nota in lista:
    if nota > notamaxima:
         notamaxima = nota

print("1)cantidad de notas: ", cantidad,
       "2)el promedio es: ",promedio,
        "3)nota minima: ", notaminima,
         "4) nota maxima: ", notamaxima )








