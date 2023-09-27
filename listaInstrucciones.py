from nodoInstrucciones import nodoInstrucciones
from CInstrucciones import CInstrucciones

class listaInstrucciones:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,CInstrucciones):
        if self.primero is None:
            self.primero=nodoInstrucciones(CInstrucciones)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoInstrucciones(CInstrucciones)

    def imprimir(self):
        
        actual=self.primero
        # print("*********Lista Instrucciones********")
        while actual!= None:
            print(f"Dron: {actual.CInstrucciones.dron_actual}, Posicion: {actual.CInstrucciones.posicion}")
            actual=actual.siguiente
        print("---------------------------------------------------------")
    
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