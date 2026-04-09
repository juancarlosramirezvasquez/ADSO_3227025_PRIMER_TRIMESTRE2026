# Agregar nuevos clientes
def agregar_cliente(lista_clientes, nombre):
    # Verificamos si el dato ingresado sea una cadena y longitud valida entre 2 a 50 caracteres
    if isinstance(nombre, str) and 2 <= len(nombre) <= 50:
        # si el nombre cumple
        lista_clientes.append(nombre.title())
        print(f"Cliente agregado: {nombre.title()}")
    else: # si el nombre ingresado no cumple la validacion entonces:
        print("Nombre del cliente invalido debe tener entre 2 a 50 caracteres")

# Recorrer la lista y mostrar todos los datos
def mostrar_clientes(lista_clientes):
    for cliente in lista_clientes:
        print(f"- {cliente}")

# Modificar un nombre en caso de error
def modificar_cliente(lista_clientes, indice, nuevo_nombre):
    # Verificamos si el dato ingresado sea una cadena y longitud valida entre 2 a 50 caracteres
    if not isinstance(nuevo_nombre, str) or not (2 <= len(nuevo_nombre) <= 50):
        print("Nombre del cliente invalido debe tener entre 2 a 50 caracteres")
        return

    if 0 <= indice < len(lista_clientes):
        original = lista_clientes[indice]
        lista_clientes[indice] = nuevo_nombre.title()
        print(f"El cliente {original} fue modificado por: {nuevo_nombre.title()}")
    else:
        print("No existe ese cliente en la lista")

# Eliminar un cliente
def eliminar_cliente(lista_clientes, indice):
    if 0 <= indice < len(lista_clientes):
        eliminado = lista_clientes.pop(indice)
        print(f"Cliente eliminado: {eliminado}")
    else:
        print("Ese cliente no existe en nuestro sistema")

def main():
    clientes = ["Kelly", "Cristian", "Nelson", "Sra Pava", "Naño", "Sebastian"]
    
    print("Clientes activos:")
    mostrar_clientes(clientes)
    
    print("\n--- Agregando cliente ---")
    agregar_cliente(clientes, "alejandro")
    
    print("\nClientes activos mas el nuevo:")
    mostrar_clientes(clientes)
    
    print("\n--- Modificando cliente ---")
    modificar_cliente(clientes, 4, "gabriela")
    mostrar_clientes(clientes)
    
    print("\n--- Eliminando cliente ---")
    eliminar_cliente(clientes, 3)
    mostrar_clientes(clientes)

if __name__ == "__main__":
    main()