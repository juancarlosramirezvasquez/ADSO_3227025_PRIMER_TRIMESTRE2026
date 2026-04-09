class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio
    @property
    def precio(self):
        return self.__precio  
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str):
            self.__titulo =  nuevo_titulo
    @precio.setter
    def precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser un numero positivo")

def main():
    Libro = Libro("El coronel", 3232)
    print(Libro.precio) 