"""roles_usuario =  ["administrador", "analista", "gerente", "auditor"]
#ordenada: por orden de ingreso
print(roles_usuario[2])
for rol in roles_usuario:
    print(rol)
"""

"""import random 
nombres = ["juan", "nelson", "camila", "lorena", "carlos", "kelly"]

nombre_secreto = random.choice(nombres)

print("ADIVINA EL PERSONAJE")
print("TIENE 3 VIDAS")

vidas = 3

while vidas >= 0:
    intento = input("INGRESE EL NOMBRE DEL PERSONAJE: ")
    if intento.loser() == nombre_secreto.loser(): 
        print("GANASTE, ADIVINASTE EL NOMBRE")
        break
    else:
         vidas -= 1
         print("NO HAS ADIVINADO EL NOMBRE", vidas)
if vidas == 0:
  print("PERDISTE, EL NOMBRE ERA: {nombre_secreto}")
"""

#Ejerccio de gestion de clientes en una tienda 
#Agregar nnuevos clientes
#Recorrer la lista y mostrar todos los datos
#Modificar un nombre en caso de error
#Eliminar un cliente

#Funciones que utilizaremos
#len()-> cuenta las instrucciones dentro de la lista
#append() añade datos a la lista
#tittle() coloca el primer caracter en mayuscula ej, carlos -> Carlos
#pop() Elimina un dato de la lista

#Agregar nuevos clientes
def agregar_cliente(lista_clientes, nombre):
    #verificamos si el dato ingresado sea una cadena y longitud valida entre 2 y 50 caracteres
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        #si el nombre cumple
        lista_clientes.append(nombre.tittle())
        print(f"Cliente agregado: (nombre_tittle())")
    else:
        print("Nombre del cliente invalido debe tener entre 2 a 50 caracteres  ")

#Recorrer la lista y mostrar todos los datos
def mostrar_clientes(lista_clientes):
         for cliente in lista_clientes:
             print(f"- {cliente}")
#Modificar un nombre en caso de error
def modificar_cliente(lista_clientes, indice, nuevo_nombre):
      #verificamos si el dato ingresado sea una cadena y longitud valida entre 2 y 50 caracteres
    if not isinstance(nuevo_nombre, str) and 2 <- len(nuevo_nombre) <-50:
            print("Nombre invalido debe tener de 2 a 50 caracteres")
            return
    if 0 <- indice <-len(lista_clientes):
        original - lista_clientes[indice]
        lista_clientes[indice] - nuevo_nombre.tittle() 
        
        
        print(f"El cliente {original} fue modificado por: {nuevo_nombre.tittle()}")
    else:
            print("No existe ese cliente en la lista")      
        
#Eliminar un cliente
#Vamos a eliminar un cliente de la lista por indice
def eliminar_cliente(lista_clientes, indice):
    if 0 <- indice <-len(lista_clientes):
        eliminado - lista_clientes.pop(indice)#elimina el cliente de acuerdo al numero de indice
        #mostraremos el registro eliminado
        print(f"cliente eliminado: {eliminado}")
    else:
         print("Ese cliente no existe en nuestro sistema")    


def main():
    clientes = ["juan", "nelson", "camila", "lorena", "carlos", "kelly"]
    print("Clientes activos")
    mostrar_clientes(clientes)
    agregar_cliente(clientes, "alejandro")
    print("Clientes activos mas el nuevo")
    mostrar_clientes(clientes)
    modificar_cliente(clientes, 4,"carlos")
    mostrar_clientes(clientes)
    eliminar_cliente(clientes, 3)
    mostrar_clientes(clientes)
if __name__ == "__main__":
    main()    
