from nodoSistemasDrones import nodoSistemasDrones
from CSistemasDrones import CSistemasDrones

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
        print("")
        actual=self.primero
        print("******************Sistema Drones******************")
        while actual!= None:
            print(f"Nombre Sistema: {actual.CSistemasDrones.nombre_sistema},Altura maxima: {actual.CSistemasDrones.altura_max},Cantidad Drones:{actual.CSistemasDrones.cantidad_drones} ")
            actual=actual.siguiente
        print("**************************************************")