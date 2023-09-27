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