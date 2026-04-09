class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio
    #Vamos a crear getter, permite acceder al valor del atributo de manera segura
    
    def get__titulo(self):
        return self.__titulo
    def get__precio(self):
        return self.__precio
    
    # Vamos a controlar, validar valores anter de ser modificados

    def set_titulo(self, nuevo_titulo):
        if isinstance (nuevo_titulo, str) and nuevo_titulo != "":
            self.__titulo = nuevo_titulo
        else:
            print("Error en el titulo ingresado, debe ser valido")
    def set_precio(self, nuevo_precio):
        if isinstance (nuevo_precio, (int, float)) and nuevo_precio >=0:
            self.__precio = nuevo_precio
        else:
            print("Error en el precio ingresado, debe ser vaalido")
    def mostrar_info(self):
        print(f"Tituo libro:{self.__titulo}")
        print(f"precio: ${self.__precio}")

def main():
    print("========S.I Libros complejo sur========")
    Libro1=Libro("Pedro Paramo", 70000)
    print("=== Información del Libro ===")
    Libro1.mostrar_info()

    print("\n Precio nuevo libro: $", Libro1.get__precio())




if __name__ == "__main__":
        main()