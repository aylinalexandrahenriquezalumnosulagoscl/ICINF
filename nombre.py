def main():
    nombre1 = input("Ingrese el primer nombre: ")
    nombre2 = input("Ingrese el segundo nombre: ")

    nombres_ordenados = sorted([nombre1, nombre2])

    print("Los nombres ordenados alfabéticamente son:")
    for nombre in nombres_ordenados:
        print(nombre)

if __name__ == "__main__":
    main()
