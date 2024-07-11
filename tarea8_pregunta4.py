def sumatoria(numero):
    if numero == 1:
        return 1
    else:
        return numero + sumatoria(numero - 1)

numero_ejemplo = 5
resultado = sumatoria(numero_ejemplo)
print("La sumatoria de los números desde 1 hasta ",numero_ejemplo, "es:", resultado)
