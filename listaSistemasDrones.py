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