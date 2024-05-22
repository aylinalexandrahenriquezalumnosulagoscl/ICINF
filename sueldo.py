def main():
    sueldos = [] 
    while True:
        sueldo = float(input("Ingrese el sueldo del empleado (-1 para terminar): "))
        if sueldo == -1:
            break
        sueldos.append(sueldo)

    empleados_500_900 = sum(1 for sueldo in sueldos if 500000 <= sueldo <= 900000)
    empleados_mas_900 = sum(1 for sueldo in sueldos if sueldo > 900000)

    gasto_total = sum(sueldos)

    print("Cantidad de empleados que cobran entre $500.000 y $900.000:", empleados_500_900)
    print("Cantidad de empleados que cobran más de $900.000:", empleados_mas_900)
    print("Gasto total de la empresa en sueldos: ${:,.2f}".format(gasto_total))

if __name__ == "__main__":
    main()
