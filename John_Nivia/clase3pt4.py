class Operacion():
    def __init__(self, numero1, numero2):
        self.numero1 =numero1
        self.numero2 = numero2
        print("**** Alerta,  BEEP BEEP ----   iNICIANDO LA OPERACION ****")
    def calcular(self):
        print("**** REALIZANDO OPERACIONES GENERICAS ****")
class Suma(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("****PREPARANDO OPERACION SUMA****")
    def calcular(self):
        super().calcular()
        resultado = self.numero1 + self.numero2
        print(f"El resultado de la suma es: {resultado}")     
class Resta(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("**** Preparando operacicon ****")
    def calcular(self):
        super().calcular()
        resultadores = self.numero1 - self.numero2
        print(f"El resultado de la operecion es: {resultadores}")
class multiplicacion(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("**** Preparando operacicon ****")
    def calcular(self):
        super().calcular()
        resultadomul= self.numero1 * self.numero2
        print(f"El resultado de la operecion es: {resultadomul}")
class dividir(Operacion):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
        print("**** Preparando operacicon ****")
    def calcular(self):
        super().calcular()
        resultadodiv = self.numero1 / self.numero2
        if resultadodiv == 0:
            print("ingrese un numero valido")
        else:
            print(f"El resultado de la operecion es: {resultadodiv}")


def main():

    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese un numero: "))

    Operacion1 = Suma(num1, num2)
    Operacion1.calcular()
    print("Alerta operacion ya sin peligro")

    Operacion1 = Resta(num1, num2)
    Operacion1.calcular()
    print("Alerta operacion ya sin peligro")

    Operacion1 = multiplicacion(num1, num2)
    Operacion1.calcular()
    print("Alerta operacion ya sin peligro")

    Operacion1 = dividir(num1, num2)
    Operacion1.calcular()
    print("Alerta operacion ya sin peligro")

if __name__ == "__main__":
    main()
