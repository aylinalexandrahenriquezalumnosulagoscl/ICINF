def calcular_nivel(total_preguntas, preguntas_correctas):
    porcentaje = (preguntas_correctas / total_preguntas) * 100

    if porcentaje >= 95:
        print("Nivel máximo")
    elif porcentaje >= 70:
        print("Nivel medio")
    elif porcentaje >= 40:
        print("nivel regular")
    else:
        print( "Fuera de nivel")
    
total_preguntas = int(input("Ingrese el total de preguntas: "))
preguntas_correctas = int(input("Ingrese la cantidad de preguntas respondidas correctamente: "))

nivel = calcular_nivel(total_preguntas, preguntas_correctas)
