#crear un programa de phyton que permita ingresar al usuario 5 paises(clave)
#que ud. elija, con sus respectivas capitales(valor ) en un diccionario
#de  datos. una vez ingresado lo anterior, debera solicitar el nombre del 
#turista  y sus paises de procedencia.para finalizar, con todos los datos
#previamente ingresados,el programa debera completar el texto con el siguiente
#formato: "el turista con el nombre XXXXX  viene del pais YYYYY y su capital
#es ZZZZZ"
# Diccionario de países y capitales
paises_capitales = {}

for pais in range(5):
    pais = input("Ingrese el nombre del pais : ")
    clave = input("Ingrese la clave para el pais: ")
    paises_capitales[pais] = clave


nombre_turista = input("Ingrese el nombre del turista: ")

pais = input("Ingrese el país de procedencia del turista: ")


print("el turista con el nombre ", nombre_turista, "viene del ", pais, "y su capital es ",
       paises_capitales[pais])


