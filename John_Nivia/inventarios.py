"""
.append() agregar
.insert()
.remove() / pop()
.sort() ordenar
.invertir() invertir los valores
"""

def mostrar_inventario(productos):
    print("mostrar inventario")
    if not productos:
        print("No hay productos registrados")
        return
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f}")

def agregar_producto(productos, nombre, precio):
    #validacion de entrada
    if (
    isinstance(nombre, str) and nombre.strip() and isinstance
    (precio, (int, float)) and precio > 0
    ):
        productos.append ({"nombre":nombre.title(), "precio": precio})
        print(f"producto '{nombre.title()}' agregado.")
    else:
        print("Producto no agreagado, datos invalidos, pene, el valor debe ser un numero positivo")

def insertar_productos(productos, indice, nombre, precio):
    if 0 <= indice <= len(productos) and isinstance(precio, (int, float)) and precio > 0:
        productos.insert(indice, {"nombre":nombre.title(), "precio": precio})
        print(f"producto '{nombre.title()}'insertado en posicion {indice+1}.")
    else:
        print("Indice o precio invalido")
if __name__ == "__main__":
    #Inventario inicial
        inventario = [
        {"nombre": "Taladro","precio":1500000},
        {"nombre": "Martillo","precio":1500000},
        {"nombre": "Destornillador","precio":1500000}
    ]
    #Mostrar inventario
mostrar_inventario(inventario)

    #Agregar productos
agregar_producto(inventario, "dildo circular", 220000)
mostrar_inventario(inventario)