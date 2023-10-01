from nodoMovimientos import nodoMovimientos
from CMovimientos import CMovimientos


class listaMovimientos:
    def __init__(self):
        self.primero = None
        self.ultimo = None


    def insertar(self,CMovimientos):
        if self.primero is None:
            self.primero=nodoMovimientos(CMovimientos)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoMovimientos(CMovimientos)
    
    def get_alturaDron(self,dron):
        actual = self.primero
        ultima_altura = 0
        while actual!= None:
            if dron == actual.CMovimientos.dron:
                # return print("Altura encontrada")
                ultima_altura = actual.CMovimientos.altura
            actual = actual.siguiente
        return ultima_altura
    
    def existe_dron(self,dron):
        actual = self.primero
        existeDron = False
        while actual!= None:
            if dron == actual.CMovimientos.dron:
                # return print("Altura encontrada")
                existeDron = True
            actual = actual.siguiente
        return existeDron

    def eliminar_datos(self):
        while self.primero:
            actual = self.primero
            self.primero = self.primero.siguiente
            del actual
    
    
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