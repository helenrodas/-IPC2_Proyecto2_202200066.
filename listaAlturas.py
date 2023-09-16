from nodoAlturas import nodoAlturas
from CAlturas import CAlturas

class listaAlturas:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,CAlturas):
        if self.primero is None:
            self.primero=nodoAlturas(CAlturas)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoAlturas(CAlturas)

    def imprimir(self):
        print("")
        actual=self.primero
        print("--------Alturas--------")
        while actual!= None:
            print(f"Altura: {actual.CAlturas.altura}, Letra: {actual.CAlturas.letra}")
            actual=actual.siguiente
        print("-----------------------")