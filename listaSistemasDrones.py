from nodoSistemasDrones import nodoSistemasDrones
from CSistemasDrones import CSistemasDrones
from listaContenido import listaContenido

class listaSistemasDrones:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,CSistemasDrones):
        if self.primero is None:
            self.primero=nodoSistemasDrones(CSistemasDrones)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoSistemasDrones(CSistemasDrones)

    def imprimir(self):
        actual=self.primero
        print("")
        print("*********************Sistema Drones*********************")
        while actual!= None:
            print("---------------------------------------------------------")
            print(f"Nombre Sistema: {actual.CSistemasDrones.nombre_sistema}, Altura maxima: {actual.CSistemasDrones.altura_max}, Cantidad Drones: {actual.CSistemasDrones.cantidad_drones} ")
            print("---------------------------------------------------------")
            actual.CSistemasDrones.listaContenido.imprimir()
            actual=actual.siguiente
        print("********************************************************")
    
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