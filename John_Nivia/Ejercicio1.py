class Mueble:
    def __init__(self, material, color, tamaño, peso, nombre ):
        self.__material = material
        self.__color = color
        self.__tamaño = tamaño
        self.__peso = peso
        self.__nombre = nombre
    def get_material(self):
        return self.__material
    def get_color(self):
        return self.__color
    def get_tamaño(self):
        return self.__tamaño
    def get_peso(self):
        return self.__peso
    def get_nombre(self):
        return self.__nombre
    
    def set_material(self, nuevo_material):
        if isinstance(nuevo_material, {str})and nuevo_material == ("madera","metal"):
            self.__material = nuevo_material
        else:
            print("Ese no es un material adecuado")
    def set_color(self, nuevo_color):
        if isinstance(nuevo_color, {str})and nuevo_color == ("azul", "amarillo", "rojo"):
            self.__color = nuevo_color
        else:
            print("Ingrese solo los colores primarios")
    def set_tamaño(self, nuevo_tamaño):
        if isinstance(nuevo_tamaño, {int, float}) and nuevo_tamaño > 0:
            self.__tamaño = nuevo_tamaño
        else:
            print("Ingrese un tamaño adecuado")
    def set_peso(self, nuevo_peso):
        if isinstance(nuevo_peso, {int, float}) and nuevo_peso > 0:
            self.__peso = nuevo_peso
        else:
            print("Ingrese un peso adecuado")
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, {str})and nuevo_nombre == ("silla", "mesa", "puerta"):
            self.__nombre = nuevo_nombre
        else:
            print("Ingrese un mueble aceptable")


    def main():
        print("=============Bienvenido a la carpinteria===============")

        Mueble1 = Mueble("madera", "azul", 2, 3, "silla")
        Mueble2 = Mueble("metal", "rojo", "5", "6", "Mesa")


        print("\n Informacion del primer mueble")
        print(f"El material del primer mueble es {Mueble.get_material()}")
        print(f"El color del primer mueble es {Mueble.get_color()}")
        print(f"El tamaño del primer mueble es {Mueble.get_tamaño()}mts")
        print(f"El nombre del primer mueble es {Mueble.get_nombre()}")

        Mueble1.mostrar_info()    

    if __name__ == "__main__":
        main()