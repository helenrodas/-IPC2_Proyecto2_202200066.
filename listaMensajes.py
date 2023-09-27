from nodoMensajes import nodoMensajes
from CMensajes import CMensajes

class listaMensajes:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    # def insertar(self,CMensajes):
    #     if self.primero is None:
    #         self.primero=nodoMensajes(CMensajes)
    #         return
    #     actual=self.primero
    #     while actual.siguiente:
    #         actual=actual.siguiente
    #     actual.siguiente=nodoMensajes(CMensajes)
        
    def insertar(self,CMensajes):
        nuevo_nodo = nodoMensajes(CMensajes)
        
        if self.primero is None or CMensajes.nombre_mensaje < self.primero.CMensajes.nombre_mensaje:
            nuevo_nodo.siguiente = self.primero
            self.primero=nuevo_nodo
            return
        actual=self.primero
        while actual.siguiente and actual.siguiente.CMensajes.nombre_mensaje < CMensajes.nombre_mensaje:
            actual=actual.siguiente
        nuevo_nodo.siguiente = actual.siguiente
        actual.siguiente=nodoMensajes(CMensajes)

    def imprimir(self):
        actual=self.primero
        # print("*********Lista Contenido********")
        while actual!= None:
            print("----------------------------------------")
            print(f"Nombre Mensaje: {actual.CMensajes.nombre_mensaje}, Sistema Drones: {actual.CMensajes.sistema_drones}")
            print("----------------------------------------")
            actual.CMensajes.listaInstrucciones.imprimir()
            actual=actual.siguiente
    
    
    def encontrar_sistema(self,nombre):
        actual = self.primero
        while actual!= None:
            if nombre == actual.CMensajes.sistema_drones:
                return actual.CMensajes.listaInstrucciones
            actual = actual.siguiente
    
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