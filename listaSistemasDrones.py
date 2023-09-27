from nodoSistemasDrones import nodoSistemasDrones
from CSistemasDrones import CSistemasDrones
from listaContenido import listaContenido
import os

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
    
    def encontrar_listaContenido(self,sistema):
        actual = self.primero
        while actual!= None:
            if sistema == actual.CSistemasDrones.nombre_sistema:
                # return print("Altura encontrada")
                return actual.CSistemasDrones.listaContenido
            actual = actual.siguiente
    
    def generar_dot(self):
        dot_code = """
        
        """

        aux = self.primero
        while aux:
            dot_code += f"""
                <tr>
                    <td>{aux.CSistemasDrones.nombre_sistema}</td>
                </tr>
                """+aux.CSistemasDrones.listaContenido.generar_dot()+aux.CSistemasDrones.listaAlturasSistema.generar_dot()+"""
            """
            aux = aux.siguiente

        
        return dot_code

    def recorrer_grafica(self):
        f = open('bb.dot','w')

        dot_code = f"""
        digraph G {{
            node [shape=box];
            tbl [label=<<table border="0" cellborder="1" cellspacing="0">{self.generar_dot()}</table>>];
        }}
        """

        f.write(dot_code)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f"dot -Tpng bb.dot -o Sistema.png")
    
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