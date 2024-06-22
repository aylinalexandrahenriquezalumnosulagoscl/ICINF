# Crear un programa que a partir de un diccionario “supermercado” permita
#que el usuario ingrese N productos, compuestos por el nombre del producto
#(clave) y la cantidad del mismo (valor). Para finalizar, deberá ingresar
#un vacío (Enter). Al finalizar, deberá solicitar ingresar un valor numérico
#X y mostrar todos los nombres de productos ingresados con sus respectivas
#cantidades multiplicadas por X.

supermercado={}
while True:
    n=input("Ingrese producto(enter para finalizar ")
    if n=="":
        break
    m=int(input("ingrese cantidad del producto"))
    supermercado[n]=m

x=int(input("ingrese un valor numerico"))
for n, m in supermercado.items():
        multiplicacion = m * x
        print(f"Producto: {n}, Cantidad: {multiplicacion}")