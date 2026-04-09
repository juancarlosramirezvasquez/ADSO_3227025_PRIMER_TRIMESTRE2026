from logging import setLogRecordFactory
class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def validar(self):
        if not isinstance(self.a,(int,float)) or not isinstance(self.b,(int,float)):
            raise ValueError("los valores numeros debe ser numericos}")
    def mostrar_datos(self):
        print(f"Valores recibidos: {self.a} y {self.b}")
    def calcular(self):
        print("Realizando operacion matematica...")
class Suma(Operacion):
    def calcular(self):
        super().validar()
        super().mostrar_datos()
        super().calcular()
        resultado = self.a + self.b
        print(f"El resultado es: {resultado}")
def main():
    num1= float(input("Ingrese un numero: "))
    num2= float(input("Ingrese un numero: "))
    operacion1 = Suma(num1, num2)
    operacion1.calcular()
if __name__ == "__main__":
    main()

