from abc import ABC, abstractmethod
from  typing import Optional

class Movilble(ABC):
    @abstractmethod
    def mover(self) -> None:
        pass
class Animal(ABC):
    def __init__(self, nombre: str) -> None:
        self.__nombre: str = ""
        self.nombre = nombre

#GETTER = MOSTRAR
    @property
    def nombre(self) -> None:   
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str ) -> None:
        if  isinstance(nuevo_nombre,str) and nuevo_nombre.strip () and nuevo_nombre !="":
            self.__nombre = nuevo_nombre.strip().title()
    @abstractmethod
    def sonido (self) -> None:
        pass
class Perro(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre}El perro hace Guau Guau")
class Vaca(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre}la vaca hace Muuuuuuuuuu Muuuuuuuuuuuu")
class Gato(Animal):
    def sonido(self) -> None:
        print(f"{self.nombre}El gato hace miau miua")
class Leon(Animal, Movilble):
    def sonido(self) -> None:
        print(f"{self.nombre}El leon  dice: rooooar")
    def mover(self) -> None:
        print(f"{self.nombre}El leon se mueve sigilosamente por el SENA")
#Realizaremos la funciones polimorficas
def hacer_sonido(animal: Animal) -> None:
    animal.sonido()
def desplazar(animal: Movilble) -> None:
    animal.mover()
def main():
    try:
        animales = [
            Perro("Rocky"),
            Gato("Misu"),
            Vaca("Lola"),
            Leon("Simba")
        ]
        print("===== Polimorfismo en nuestro zoologico =====")
        for animal in animales:
            hacer_sonido(animal)
            print("Animales con movimiento")
    except ValueError as e:
        print(f"ERROR, {e}")

if  __name__ == "__main__":
    main()
