from nodoDron import nodoDron
from CDron import CDron

class listaDrones:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def insertar(self,CDron):
        if self.primero is None:
            self.primero=nodoDron(CDron)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoDron(CDron)

    def imprimir(self):
        print("")
        actual=self.primero
        print("*********Lista Drones********")
        while actual!= None:
            print("Dron:",actual.CDron.nombre_dron)
            actual=actual.siguiente
        print("*****************************")