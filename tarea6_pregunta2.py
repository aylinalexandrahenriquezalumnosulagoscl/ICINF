#Crear un programa en Python, que permita dentro de un bucle principal (ej: bucle while), el
#siguiente menú de opciones:
#- Ingresar un elemento a la lista
#- Modificar un elemento de la lista según el índice
#- Eliminar un elemento de la lista según el índice
#- Eliminar el último elemento de la lista
#- Buscar un elemento de la lista según el dato (devuelve el índice)
#- Mostrar todos los elementos de la lista
#-Salir (salir del bucle principal y finalizar)
lista=[]

def ingresar_elemento(lista):
    elemento = input("Ingrese el elemento a agregar a la lista: ")
    lista.append(elemento)
    print("Elemento agregado")

def modificar_elemento(lista):
    indice = int(input("Ingrese el indice del elemento para modificar: "))
    if indice < 0 or indice >= len(lista):
        print("error.")
    else:
        nuevo_valor = input("Ingrese el nuevo valor para el elemento: ")
        lista[indice] = nuevo_valor
        print("Elemento modificado")
def eliminar_elemento(lista):
    indice = int(input("Ingrese el índice del elemento a eliminar: "))
    if indice < 0 or indice >= len(lista):
        print("Índice fuera de rango.")
    else:
        del lista[indice]
        print("Elemento eliminado correctamente.")

def eliminar_ultimo(lista):
    if lista:
        elemento_eliminado = lista.pop()
        print(f"Se eliminó el elemento '{elemento_eliminado}' de la lista.")
    else:
        print("La lista está vacía.")

def buscar_elemento(lista):
    elemento = input("Ingrese el elemento para buscar: ")
    try:
        indice = lista.index(elemento)
        print(f"El elemento '{elemento}' se encuentra en el índice {indice}.")
    except ValueError:
        print(f"El elemento '{elemento}' no se encuentra en la lista.")

def mostrar_elementos(lista):
    if lista:
        print("Elementos en la lista:")
        for i, elemento in enumerate(lista):
            print(f"{i}: {elemento}")
    else:
        print("La lista está vacía.")
def main():
    lista = []
    while True:
        print("opciones:")
        print("1. Ingresar un elemento a la lista")
        print("2. Modificar un elemento de la lista según el índice")
        print("3. Eliminar un elemento de la lista según el índice")
        print("4. Eliminar el último elemento de la lista")
        print("5. Buscar un elemento de la lista según el dato")
        print("6. Mostrar todos los elementos de la lista")
        print("7. Salir")
        
        opcion = input("Ingrese el número de la opción que desea realizar: ")
        
        if opcion == "1":
            ingresar_elemento(lista)
        elif opcion == "2":
            modificar_elemento(lista)
        elif opcion == "3":
            eliminar_elemento(lista)
        elif opcion == "4":
            eliminar_ultimo(lista)
        elif opcion == "5":
            buscar_elemento(lista)
        elif opcion == "6":
            mostrar_elementos(lista)
        elif opcion == "7":
            print("bye")
            break
        else:
            print("Opción no válida.")