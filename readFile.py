import xml.etree.ElementTree as ET
from listaDrones import listaDrones
from listaSistemasDrones import listaSistemasDrones
from listaContenido import listaContenido
from listaAlturas import listaAlturas
from CAlturas import CAlturas
from CContenido import CContenido
from CDron import CDron
from CSistemasDrones import CSistemasDrones

class readFile():
    def __init__(self):
        self.lista_drones_temp = listaDrones()
        self.lista_sistemas_temp = listaSistemasDrones()
    
    def cargarXml(self):
        try:
            with open("entradaV3.xml", encoding='utf-8') as xml_file:
                root = ET.fromstring(xml_file.read())
                NodoListaDrones = root.findall('listaDrones') 
                for nodoDron in NodoListaDrones:
                    lista_nombre_dron = nodoDron.findall('dron')
                    for nombre_dron in lista_nombre_dron:
                        nombre = nombre_dron.text
                        nombre_agregado = CDron(nombre)
                        self.lista_drones_temp.insertar(nombre_agregado)
                self.lista_drones_temp.imprimir()
                NodoListaSistemasDrones = root.findall('listaSistemasDrones')
                for nodoSistemas in NodoListaSistemasDrones:
                    lista_sistemas = nodoSistemas.findall('sistemaDrones')
                    for sistemas in lista_sistemas:
                        nombre_sistema = sistemas.get('nombre')
                        # print("nombre sistema: ",nombre_sistema)

                        lista_altura_max = sistemas.findall('alturaMaxima')
                        for nodo_altura_max in lista_altura_max:
                            altura_max = nodo_altura_max.text
                            # print("altura Maxima: ",altura_max)
                        
                        lista_cantidad_drones = sistemas.findall('cantidadDrones')
                        for nodo_cantidad_drones in lista_cantidad_drones:
                            cantidad_drones = nodo_cantidad_drones.text
                            # print("cantidad:",cantidad_drones)
                        self.lista_sistemas_temp.insertar(CSistemasDrones(nombre_sistema,altura_max,cantidad_drones))
                    # self.lista_sistemas_temp.imprimir()
                        lista_contenido = sistemas.findall('contenido')
                        self.lista_contenido_temp = listaContenido()
                        for nodo_contenido in lista_contenido:
                            dron_actual = nodo_contenido.find('dron')
                            dron = dron_actual.text
                            
                            self.lista_contenido_temp.insertar(CContenido(dron))
                            lista_alturas = nodo_contenido.findall('alturas')
                            self.lista_alturas_temp = listaAlturas()
                            for nodo_alturas in lista_alturas:
                                lista_altura = nodo_alturas.findall('altura')
                                for nodo_altura in lista_altura:
                                    altura = nodo_altura.get('valor')
                                    letra = nodo_altura.text
                                    self.lista_alturas_temp.insertar(CAlturas(altura,letra))
                                self.lista_alturas_temp.imprimir()
                        self.lista_contenido_temp.imprimir()
                    self.lista_sistemas_temp.imprimir()
                                
        except Exception as err:
            print("Error:", err)
    

app = readFile()
app.cargarXml()