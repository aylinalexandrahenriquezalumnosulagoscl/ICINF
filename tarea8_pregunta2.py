def area_circulo(radio):
    pi = 3.14159
    area = pi * (radio ** 2)
    return area


radio_del_circulo = 5
area_del_circulo = area_circulo(radio_del_circulo)
print("El área del círculo con radio",radio_del_circulo,"es:", area_del_circulo)
