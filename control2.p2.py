#escriba un programa en python que permita ingresar 7 nombres de personas de una lista.
#una vez terminado el ingreso debera eliminar de la lista todos los nombres que termine con "a" 
#y mostrar la lista resultante despues de dicha eliminacion

nombres = []

for i in range(7):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    print("Lista antes de la eliminación:", nombres)

for nombre in (nombres ):
   if nombre.pop("a"):
      print("Lista después de la eliminación:", nombres)

