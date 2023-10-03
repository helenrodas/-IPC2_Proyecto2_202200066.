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
    
    def get_listaAlturas(self,dron):
        actual = self.primero
        while actual!= None:
            if dron == actual.CContenido.dron:
                return actual.CContenido.listaAlturas
            actual = actual.siguiente
    
    
    def generar_dot(self):
        dot_code = """
        
            <tr>
                
        <td>Altura</td>
                
        """

        aux = self.primero
        while aux:
            dot_code += f"""
                
                    
                    <td>{aux.CContenido.dron}</td>
                    

            """
            aux = aux.siguiente
        dot_code += f"""
            
        </tr>
        """

        actual1 = self.primero
        dot_code += """<tr><td border="0"></td>"""
        while actual1:
            dot_code += """
            
            
            """   
            actual1 = actual1.siguiente
        dot_code += "</tr>"

        return dot_code
    
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