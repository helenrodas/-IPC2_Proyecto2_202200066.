from nodoContenido import nodoContenido
from CContenido import CContenido
from listaAlturas import listaAlturas

class listaContenido:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,CContenido):
        if self.primero is None:
            self.primero=nodoContenido(CContenido)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoContenido(CContenido)

    def imprimir(self):
        actual=self.primero
        # print("*********Lista Contenido********")
        while actual!= None:
            print(f"Dron: {actual.CContenido.dron}")
            actual.CContenido.listaAlturas.imprimir()
            actual=actual.siguiente
            print("---------------------------------------------------------")
    
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