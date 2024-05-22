def main():
    alturas = [] 
    
    while True:
        altura = float(input("Ingrese la altura en metros (0 para finalizar): "))
        if altura == 0:
            break
        alturas.append(altura)

    if alturas:
        altura_promedio = sum(alturas) / len(alturas)
        print("La altura promedio de las personas es:", altura_promedio)
    else:
        print("No se ingresaron alturas.")

if __name__ == "__main__":
    main()

