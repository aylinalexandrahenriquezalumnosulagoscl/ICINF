#una plataforma de aprendizaje en linea, de un  curso de 15 dias, evalua diariamente los alumnos
# y genera un puntaje diario de 1 a 100 para cada uno.
#crear un programa en python que permita ingresar el puntaje diario de un alumno
#(mediante el uso de listas de pythonn)para los 15 dias del curso. al finalizar el ingreso debera mostrar,
#estrictamente en el siguiente orden, primero, que dias tienen puntajes menor a 70 puntos, y segundo, que dias tienen puntaje
#mayor o igual a 70 puntos. identifique los dias mediante un numero (ej: dia 1, dia 2, dia 3... dia 15, etc)
# Creamos una lista para almacenar los puntajes diarios del alumno


lista = []
menor70 = []
mayor70 = []

for dia in range(1, 16):
    puntaje = int(input("Ingrese el puntaje del día dia:  "))
    lista.append(puntaje)


for dia, puntaje in enumerate(lista):
    if puntaje < 70:
        menor70.append(dia)
    else:
        mayor70.append(dia)


print("Días con puntajes menores a 70 puntos:")
for dia in menor70:
    print("Día", dia)

print("Días con puntajes iguales o mayores a 70 puntos:")
for dia in mayor70:
    print("Día", dia)



