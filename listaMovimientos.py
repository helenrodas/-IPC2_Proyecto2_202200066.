import os
from nodoMovimientos import nodoMovimientos
from CMovimientos import CMovimientos


class listaMovimientos:
    def __init__(self):
        self.primero = None
        self.ultimo = None


    def insertar(self,CMovimientos):
        if self.primero is None:
            self.primero=nodoMovimientos(CMovimientos)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoMovimientos(CMovimientos)
    
    def get_alturaDron(self,dron):
        actual = self.primero
        ultima_altura = 0
        while actual!= None:
            if dron == actual.CMovimientos.dron:
                # return print("Altura encontrada")
                ultima_altura = actual.CMovimientos.altura
            actual = actual.siguiente
        return ultima_altura

    def get_tiempoDron(self,dron):
        actual = self.primero
        ultima_altura = 0
        while actual!= None:
            if dron == actual.CMovimientos.dron:
                # return print("Altura encontrada")
                ultima_altura = actual.CMovimientos.tiempo
            actual = actual.siguiente
        return ultima_altura
    
    def existe_dron(self,dron):
        actual = self.primero
        existeDron = False
        while actual!= None:
            if dron == actual.CMovimientos.dron:
                # return print("Altura encontrada")
                existeDron = True
            actual = actual.siguiente
        return existeDron

    def eliminar_datos(self):
        while self.primero:
            actual = self.primero
            self.primero = self.primero.siguiente
            del actual
    
    # def generar_dot(self):
    #     dot_code = """
        
            
                
    #     <td>Tiempo</td>
                
    #     """

    #     drone_names_added = set()

    #     aux = self.primero
    #     while aux:
    #         dron = aux.CMovimientos.dron
    #         altura = aux.CMovimientos.altura
    #         movimiento = aux.CMovimientos.movimiento

    #         # Si el nombre del dron no está en la lista, agrégalo al DOT
    #         if dron not in drone_names_added:
    #             dot_code += f"""
    #                 <td bgcolor="lightgray">{dron}</td>
    #             """
    #             drone_names_added.add(dron)

    #         dot_code += f"""
    #             </tr>
    #             <tr>
    #                 <td>{altura}</td>
    #                 <td>{movimiento}</td>
    #             </tr>
    #         """

    #         aux = aux.siguiente

    #     dot_code += "</tr>"

    #     return dot_code
    
    def generar_dot(self):
        dot_code = """
        
            <tr>
                
        <td>Tiempo</td>
                
        """
        drone_names_added = set()
        aux = self.primero
        while aux:
            dron = aux.CMovimientos.dron
            if dron not in drone_names_added:
                dot_code += f"""
                
                    
                    <td>{aux.CMovimientos.dron}</td>
                    

                """
                
                drone_names_added.add(dron)
                
            dot_code += f"""
            <tr>
                <td>{aux.CMovimientos.movimiento}</td>
            """
            aux = aux.siguiente
        dot_code += f"""
            
        </tr>
        """

        dot_code += "</tr>"

        return dot_code


    def recorrer_grafica(self):
        f = open('aa.dot', 'w', encoding="utf-8")

        dot_code = f"""
        digraph G {{
            node [shape=box];
            tbl [label=<<table border="0" cellborder="1" cellspacing="0">{self.generar_dot()}</table>>];
        }}
        """

        f.write(dot_code)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f"dot -Tpng aa.dot -o Movimientos.png")
    
    
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