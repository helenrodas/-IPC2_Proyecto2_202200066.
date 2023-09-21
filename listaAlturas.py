from nodoAlturas import nodoAlturas
from CAlturas import CAlturas

class listaAlturas:
    def __init__(self):
        self.Count = 0
        self.status = ""
        self.primero = None
        self.ultimo = None
        
    def insertar(self,CAlturas):
        self.Count +=  1
        self.status = self.status + "Altura:" + CAlturas.altura + " Letra:" + CAlturas.letra + "\n"
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
        # print("--------Alturas--------")
        while actual!= None:
            print(f"Altura: {actual.CAlturas.altura}, Letra: {actual.CAlturas.letra}")
            actual=actual.siguiente
        # print("-----------------------")
    
    def encontrar_letra(self,valor):
        actual = self.primero
        while actual!= None:
            if valor == actual.CAlturas.altura:
                # return print("Altura encontrada")
                return actual.CAlturas.letra
            actual = actual.siguiente
    
    
    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is not None:
            valor_actual = self.actual
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration