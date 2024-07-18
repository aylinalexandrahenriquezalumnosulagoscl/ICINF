#Crear un programa en Python que implemente una función
#“solo_numeros(var)”, que devuelva un True si un String contiene
#solo números, de lo contrario, devuelva un False.

def solo_numeros(var):
      if len(var) == 0:
        return False
      
      digitos = "123456789"

      for x in var:
        if x in digitos:

            return True
        


print(solo_numeros("235"))  
print(solo_numeros("12"))  
print(solo_numeros("abcd"))




