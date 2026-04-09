from abc import ABC, abstractmethod
class GenerarReporte(ABC):
    @abstractmethod
    def generar_reporte(self) ->None:
        pass
class SistemaPago(ABC):
    def __init__(self, monto: float) -> None:
        self.monto =  monto
    @abstractmethod
    def procesar_pago(self) -> None:
        pass
class Pagobancario( GenerarReporte, SistemaPago):
    def generar_reporte(self) -> None:
        print("REPORTE: Pago realizado mediante sistema bancario")
    def procesar_pago(self) -> None:
        print(f"Precesando la transferencia bancaria por ${self.monto:,.2f}")
class PagoCriptomonedas(SistemaPago):
    def procesar_pago(self) -> None:
        print(f"Procesando pago en Cripto Monedas, por ${self.monto:.2f}")
class PagoenEfectivo(SistemaPago):
    def procesar_pago(self) -> None:
        print(F"Procesando pago en efectivo, por ${self.monto:.2f}")
        
def ejecutar_pago(pago:SistemaPago) -> None:
    pago.procesar_pago()
def main():
    print("========== SISTEMA DE PAGO CON INTERFASES APSTRACTAS")
    pago1 = Pagobancario(30000)
    pago2 = PagoCriptomonedas(300000)
    pago3 = PagoenEfectivo(25000)
    ejecutar_pago(pago1)
    pago1.generar_reporte()
    print("\n Ahora con criptos")
    ejecutar_pago(pago2)
    print("\n Ingrese la cantidad de plata que ingresara en el sistema ")
    ejecutar_pago(pago3)
if __name__ == "__main__":
    main()
        
        

