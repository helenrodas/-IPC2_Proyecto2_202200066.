from nodoMensajes import nodoMensajes
from CMensajes import CMensajes

class listaContenido:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,CMensajes):
        if self.primero is None:
            self.primero=nodoMensajes(CMensajes)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoMensajes(CMensajes)

    def imprimir(self):
        actual=self.primero
        # print("*********Lista Contenido********")
        while actual!= None:
            print(f"Nombre Mensaje: {actual.CMensajes.nombre_mensaje}, Sistema Drones: {actual.CMensajes.nombre_mensaje}")
            actual.CMensajes.listaInstrucciones.imprimir()
            actual=actual.siguiente
            print("---------------------------------------------------------")