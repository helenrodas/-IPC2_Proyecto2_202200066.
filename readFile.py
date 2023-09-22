import xml.etree.ElementTree as ET
from listaDrones import listaDrones
from listaSistemasDrones import listaSistemasDrones
from listaContenido import listaContenido
from listaAlturas import listaAlturas
from listaInstrucciones import listaInstrucciones
from listaMensajes import listaMensajes
from CMensajes import CMensajes
from CInstrucciones import CInstrucciones
from CAlturas import CAlturas
from CContenido import CContenido
from CDron import CDron
from CSistemasDrones import CSistemasDrones

class readFile():
    def __init__(self):
        self.lista_drones_temp = listaDrones()
        self.lista_sistemas_temp = listaSistemasDrones()
    
    def cargarXml(self,ruta):
        try:
            with open(ruta, encoding='utf-8') as xml_file:
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
                        
                        lista_cantidad_drones = sistemas.findall('cantidadDrones')
                        for nodo_cantidad_drones in lista_cantidad_drones:
                            cantidad_drones = nodo_cantidad_drones.text
                        count = 1
                        lista_alturas_sistema_temp = listaAlturas()
                        lista_contenido = sistemas.findall('contenido')
                        self.lista_contenido_temp = listaContenido()
                        for nodo_contenido in lista_contenido:
                            dron_actual = nodo_contenido.find('dron')
                            dron = dron_actual.text
                            
                            lista_alturas = nodo_contenido.findall('alturas')
                            self.lista_alturas_temp = listaAlturas()
                            for nodo_alturas in lista_alturas:
                                lista_altura = nodo_alturas.findall('altura')
                                for nodo_altura in lista_altura:
                                    altura = nodo_altura.get('valor')
                                    letra = nodo_altura.text
                                    self.lista_alturas_temp.insertar(CAlturas(altura,letra,count))
                                    lista_alturas_sistema_temp.insertar_alturas(CAlturas(altura,letra,count))
                                
                            count +=1
                            self.lista_contenido_temp.insertar(CContenido(dron,self.lista_alturas_temp))
                        self.lista_sistemas_temp.insertar(CSistemasDrones(nombre_sistema,altura_max,cantidad_drones,self.lista_contenido_temp,lista_alturas_sistema_temp))
                        lista_alturas_sistema_temp.imprimir()
                    self.lista_sistemas_temp.imprimir()

                print("*************Mensajes*************")
                NodoListaMensajes = root.findall('listaMensajes')
                for nodoMensajes in NodoListaMensajes:
                    lista_mensajes = nodoMensajes.findall('Mensaje')
                    self.lista_mensajes_temp = listaMensajes()
                    for nodo_mensajes in lista_mensajes:
                        nombre_mensaje = nodo_mensajes.get('nombre')
                        
                        lista_sistema_drones = nodo_mensajes.findall('sistemaDrones')
                        for nodo_sistema_drones in lista_sistema_drones:
                            sistema = nodo_sistema_drones.text
                        lista_instrucciones = nodo_mensajes.findall('instrucciones')
                        self.lista_instruciones_temp = listaInstrucciones()
                        for nodo_instrucciones in lista_instrucciones:
                            lista_instruccion = nodo_instrucciones.findall('instruccion')
                            for nodo_instruccion in lista_instruccion:
                                dron_instruccion = nodo_instruccion.get('dron')
                                posicion = nodo_instruccion.text
                                self.lista_instruciones_temp.insertar(CInstrucciones(dron_instruccion,posicion))
                        self.lista_mensajes_temp.insertar(CMensajes(nombre_mensaje,sistema,self.lista_instruciones_temp))
                self.lista_mensajes_temp.imprimir()
        except Exception as err:
            print("Error:", err)
    
    def get_listaDrones(self):
        return self.lista_drones_temp
    
    def get_listaSistemasDrones(self):
        return self.lista_sistemas_temp
    
    def get_listaMensajes(self):
        return self.lista_mensajes_temp
    
    def graficar(self):
        self.lista_sistemas_temp.recorrer_grafica()

    # def get_listaContenido(self):
    #     return self.lista_contenido_temp
    
    # def get_listaAlturas(self):
    #     return self.lista_alturas_temp

# app = readFile()
# app.cargarXml()