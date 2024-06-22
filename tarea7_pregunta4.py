#Crear un programa que permita crear un diccionario de datos “deudores”
#con el RUT de 5 personas (Claves) y sus respectivas deudas en pesos
#(Valores). Posteriormente, dentro de un bucle permitir ingresar el abono
#a las deudas de alguna persona identificándolo con su RUT y el monto del
#abono. Si la persona queda con un saldo de deuda 0, se eliminará del
#diccionario. Se finaliza el bucle si es que se ingresa un vacío. Al
#finalizar, se deberá mostrar las personas que quedaron deudoras y sus
#respectivos saldos de deuda.
deudores={"23454365-8":120000,"2345654-5":10000,
          "2345546-9":300000,"34567889-k":80000,"2358967-2":450000}


while True:
    rut=input("ingrese rut del deudor para el abono(enter para finalizar)")
    if rut=="":
        break

    monto_abono = int(input("Ingrese el monto del abono para RUT: "))

    deudores[rut] -= monto_abono

    
    if deudores[rut]== 0:
            del deudores[rut]
    
    print(deudores)