#Crear una función llamada area_rectangulo(base, altura) que devuelva 
#el área del rectángulo (con return) a partir de una base y una altura.
#Calcular el área de un rectángulo utilizando la función a crear para un
#rectángulo de 15 de base y 10 de altura. 

def area_rectangulo(base, altura):
    area = base * altura
    return area


baserectangulo = 15
alturarectangulo = 10

area_del_rectangulo = area_rectangulo(baserectangulo, alturarectangulo)
print("El área del rectángulo  base",baserectangulo,", altura",alturarectangulo,"es", area_del_rectangulo)
