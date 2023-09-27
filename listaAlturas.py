from nodoAlturas import nodoAlturas
from CAlturas import CAlturas

class listaAlturas:
    def __init__(self):
        self.Count = 0
        self.status = ""
        self.primero = None
        self.ultimo = None
        
    def insertar(self,CAlturas):
        self.Count +=  1
        self.status = self.status + "Altura:" + CAlturas.altura + " Letra:" + CAlturas.letra + "\n"
        if self.primero is None:
            self.primero=nodoAlturas(CAlturas)
            return
        actual=self.primero
        while actual.siguiente:
            actual=actual.siguiente
        actual.siguiente=nodoAlturas(CAlturas)

    def insertar_alturas(self, CAlturas):
        nuevo_nodo = nodoAlturas(CAlturas)

        if self.Count == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            actual = self.primero
            anterior = None
            while actual is not None and (int(actual.CAlturas.altura) < int(nuevo_nodo.CAlturas.altura) or (int(actual.CAlturas.altura) == int(nuevo_nodo.CAlturas.altura) and int(actual.CAlturas.contador) < int(nuevo_nodo.CAlturas.contador))):
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            else:
                nuevo_nodo.siguiente = actual
                anterior.siguiente = nuevo_nodo

        self.Count += 1


    def imprimir(self):
        print("")
        actual=self.primero
        # print("--------Alturas--------")
        while actual!= None:
            print(f"Altura: {actual.CAlturas.altura}, Letra: {actual.CAlturas.letra}")
            actual=actual.siguiente
        # print("-----------------------")
    
    def encontrar_letra(self,valor):
        actual = self.primero
        while actual!= None:
            if valor == actual.CAlturas.altura:
                # return print("Altura encontrada")
                return actual.CAlturas.letra
            actual = actual.siguiente
    
    def generar_dot(self):


        dot_code = f"""<tr><td border="0"></td>"""
        
        
        actual =self.primero
        sentinela_de_filas=actual.CAlturas.altura 
        fila_iniciada=False
        while actual != None:

            if int(sentinela_de_filas)!=int(actual.CAlturas.altura) :
                dot_code += f"""</tr><tr><td border="0"></td>"""
                sentinela_de_filas=actual.CAlturas.altura 
                fila_iniciada=False

                
            if fila_iniciada==False:
                fila_iniciada=True

                
                dot_code+="""<td>"""+str(actual.CAlturas.letra)+"""</td>\n"""
            else:
                dot_code+="""<td>"""+str(actual.CAlturas.letra)+"""</td>\n"""
            actual = actual.siguiente

        dot_code += f"""</tr>"""


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