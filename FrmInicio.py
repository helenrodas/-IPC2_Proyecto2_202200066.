from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from readFile import *
from readFile import readFile
from listaMensajeCreado import listaMensajeCreado
from CMensajeCreado import CMensajeCreado

class FrmInicio:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Drones")
        self.file_path = None
        self.readFile = readFile()
        self.nuevoDron = StringVar()
        self.tiempoTemp = 0
        self.cadenaTiempo = ""
        self.existeTabla = False
        self.tablaTemp = ""
        self.ultimaAltura=0
        self.lista_mensajeCreado_temp = listaMensajeCreado()

        # Menu con opciones
        self.options_frame = tk.Frame(root,bg='lightblue')
        self.options_frame.pack(side=tk.LEFT)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=150,height=500)

        #Opciones
        self.inicializacion_btn = tk.Button(self.options_frame,text='Inicializacion',font=('Bold',12),fg='black',bd=0,bg='lightblue',width=14,height=1, command=self.inicializar)
        self.inicializacion_btn.place(x=8,y=30)
        self.inicializacion_indicate = tk.Label(self.options_frame,text='',bg='#158aff')
        self.inicializacion_indicate.place(x=3,y=30,width=5,height=30)

        self.cargarArchivo_btn = tk.Button(self.options_frame,text='Cargar Archivo',font=('Bold',12),fg='black',bd=0,bg='lightblue',width=14,height=1,command=self.cargar_archivo)
        self.cargarArchivo_btn.place(x=8,y=90)
        self.cargarArchivo_indicate = tk.Label(self.options_frame,text='',bg='#158aff')
        self.cargarArchivo_indicate.place(x=3,y=90,width=5,height=30)

        self.generarArchivo_btn = tk.Button(self.options_frame,text='Generar Archivo',font=('Bold',12),fg='black',bd=0,bg='lightblue',width=14,height=1,command=self.crear_xml_salida)
        self.generarArchivo_btn.place(x=8,y=150)
        self.generarArchivo_indicate = tk.Label(self.options_frame,text='',bg='#158aff')
        self.generarArchivo_indicate.place(x=3,y=150,width=5,height=30)

        self.gestionDrones_btn = tk.Button(self.options_frame,text='Gestion Drones',font=('Bold',12),fg='black',bd=0,bg='lightblue',width=14,height=1)
        self.gestionDrones_btn.place(x=8,y=210)
        self.gestionDrones_indicate = tk.Label(self.options_frame,text='',bg='#158aff')
        self.gestionDrones_indicate.place(x=3,y=210,width=5,height=30)
        self.gestionDrones_btn.bind("<Button-1>", self.gestion_drones_menu)

        self.gestionSistemasDrones_btn = tk.Button(self.options_frame,text='Gestion Sistemas',font=('Bold',12),fg='black',bd=0,bg='lightblue',width=14,height=1,command = self.graficar_lista_drones)
        self.gestionSistemasDrones_btn.place(x=8,y=270)
        self.gestionSistemasDrones_indicate = tk.Label(self.options_frame,text='',bg='#158aff')
        self.gestionSistemasDrones_indicate.place(x=3,y=270,width=5,height=30)

        self.gestionMensajes_btn = tk.Button(self.options_frame,text='Gestion Mensajes',font=('Bold',12),fg='black',bd=0,bg='lightblue',width=14,height=1)
        self.gestionMensajes_btn.place(x=8,y=330)
        self.gestionMensajes_indicate = tk.Label(self.options_frame,text='',bg='#158aff')
        self.gestionMensajes_indicate.place(x=3,y=330,width=5,height=30)
        self.gestionMensajes_btn.bind("<Button-1>", self.gestion_mensajes_menu)

        self.ayuda_btn = tk.Button(self.options_frame,text='Ayuda',font=('Bold',12),fg='black',bd=0,bg='lightblue',width=14,height=1, command = self.ayuda)
        self.ayuda_btn.place(x=8,y=390)
        self.ayuda_indicate = tk.Label(self.options_frame,text='',bg='#158aff')
        self.ayuda_indicate.place(x=3,y=390,width=5,height=30)

        #Pagina principal que va cambiando segun la opcion
        self.main_frame = tk.Frame(root,highlightbackground='gray', highlightthickness=2)
        self.main_frame.pack(side=tk.LEFT)
        self.main_frame.pack_propagate(False)
        self.main_frame.configure(height=500,width=900)
        
        self.star_page()
    
    def gestion_drones_menu(self, event):
        button_x = self.gestionDrones_btn.winfo_rootx()
        button_y = self.gestionDrones_btn.winfo_rooty()
        button_width = self.gestionDrones_btn.winfo_width()
        button_height = self.gestionDrones_btn.winfo_height()

        menu_x = button_x + button_width
        menu_y = button_y + button_height

        gestion_drones_menu = tk.Menu(self.gestionDrones_btn, tearoff=0)

        gestion_drones_menu.add_command(label="Listado Drones", command=self.crear_tabla_listaDrones)
        gestion_drones_menu.add_separator()
        gestion_drones_menu.add_command(label="Agrega Dron", command=self.agregar_dron)

        gestion_drones_menu.post(menu_x, menu_y)
    
    
    def gestion_mensajes_menu(self, event):
        button_x = self.gestionMensajes_btn.winfo_rootx()
        button_y = self.gestionMensajes_btn.winfo_rooty()
        button_width = self.gestionMensajes_btn.winfo_width()
        button_height = self.gestionMensajes_btn.winfo_height()

        menu_x = button_x + button_width
        menu_y = button_y + button_height

        gestion_mensajes_menu = tk.Menu(self.gestionMensajes_btn, tearoff=0)

        gestion_mensajes_menu.add_command(label="Listado Mensajes", command=self.crear_tabla_listaMensajes)
        gestion_mensajes_menu.add_separator()
        gestion_mensajes_menu.add_command(label="Ver instrucciones de mensajes", command=self.mostrar_tablaMensajes)
        gestion_mensajes_menu.add_separator()
        gestion_mensajes_menu.add_command(label="Grafica instrucciones", command=self.clear_page)
        
        gestion_mensajes_menu.post(menu_x, menu_y)

    
    def star_page(self):
        start_frame = tk.Frame(self.main_frame)
        lb = tk.Label(start_frame,text="Sistema de Drones\n\nBienvenido",font=('Bold',20))
        lb.pack()
        start_frame.pack(pady=20)


    def crear_tabla_listaDrones(self):
        self.clear_page()
        listadoDrones_frame = tk.Frame(self.main_frame)
        tv = ttk.Treeview(listadoDrones_frame,columns=("colDrones"))
        tv.column("#0",width=90)
        tv.column("colDrones",width=90,anchor=CENTER)
        
        tv.heading("#0",text="No.",anchor=CENTER)
        tv.heading("colDrones", text="Drones", anchor=CENTER)
        
        lb = tk.Label(listadoDrones_frame,text="Lista de drones",font=('Bold',20))
        listado_drones = self.readFile.get_listaDrones()
        numero_dron = 0
        for i, dron in enumerate(listado_drones):
            numero_dron +=1
            tv.insert("", "end", text=numero_dron, values=(dron.CDron.nombre_dron))
        
        lb.pack()
        tv.pack()
        listadoDrones_frame.pack(pady=20)
    
    def agregar_dron(self):
        self.clear_page()
        dron=""
        agregarDron_frame = tk.Frame(self.main_frame)
        lb = tk.Label(agregarDron_frame,text="Agregar Dron\n",font=('Bold',20))
        
        nombre_lbl = Label(agregarDron_frame, text="Ingresa nombre dron: ", font=("Arial", 14), justify="center")
        nombre_input = tk.Entry(agregarDron_frame, textvariable=dron)
        agregar_btn = tk.Button(agregarDron_frame, text="Agregar", width=12, height=1, bg="LightGreen", command=lambda:self.registrar_dron(nombre_input.get()))
        # nombre_input.delete(0,'end')  Revisar este metodo porque aun no funciona
        
        lb.pack()
        nombre_lbl.pack()
        nombre_input.pack()
        agregar_btn.pack(pady=20)
        agregarDron_frame.pack(pady=20)
        
    
    def registrar_dron(self,nombreDron):
        bandera = False
        nombre_temp = nombreDron
        listado_drones = self.readFile.get_listaDrones()
    
        for i, dron in enumerate(listado_drones):
            if nombre_temp == dron.CDron.nombre_dron:
                bandera = True
                messagebox.showinfo("Error", "el dron ya se encuentra en la lista.")
            
        if bandera == False:
            print(nombre_temp, "=", dron.CDron.nombre_dron)
            dron_nuevo = CDron(nombre_temp)
            listado_drones.insertar(dron_nuevo)
            messagebox.showinfo("Agregar Dron", "Dron agregado exitosamente.")
            listado_drones.imprimir()
            return True
        else:
            return False
        
    
    def crear_tabla_listaMensajes(self):
        self.clear_page()
        listaMensajes_frame = tk.Frame(self.main_frame)
        tvMensajes = ttk.Treeview(listaMensajes_frame,columns=("colMensajes"))
        tvMensajes.column("#0",width=90)
        tvMensajes.column("colMensajes",width=90,anchor=CENTER)
        
        tvMensajes.heading("#0",text="Nombre",anchor=CENTER)
        tvMensajes.heading("colMensajes", text="Sistema", anchor=CENTER)
        
        lb = tk.Label(listaMensajes_frame,text="Lista de Mensajes",font=('Bold',20))
        listado_mensajes = self.readFile.get_listaMensajes()
        
        for i, mensaje in enumerate(listado_mensajes):
            tvMensajes.insert("", "end", text=(mensaje.CMensajes.nombre_mensaje), values=(mensaje.CMensajes.sistema_drones))
        
        def item_selected(event):
            for selected_item in tvMensajes.selection():
                item = tvMensajes.item(selected_item)
                valuesList = item['values']
                if valuesList:
                    sistema = valuesList[0]
                    print(sistema)

                    listaImstrucciones = listado_mensajes.encontrar_sistema(sistema)
                    
                    self.crear_tabla_listaInstrucciones(listaImstrucciones)
                
        tvMensajes.bind('<<TreeviewSelect>>',item_selected)
        
        lb.pack()
        tvMensajes.pack()
        tvMensajes.pack(side="left") 
        listaMensajes_frame.pack(pady=20)
    
    
    def crear_tabla_listaInstrucciones(self,listaInstrucciones):
        
        listaMensajes_frame = tk.Frame(self.main_frame)
        
        # if self.existeTabla == True:
        #     # print("Entro")
        #     listaMensajes_frame.destroy()
        #     listaMensajes_frame = tk.Frame(self.main_frame)
        # else:
        #     pass
        
        tvInstrucciones = ttk.Treeview(listaMensajes_frame,columns=("colInstrucciones"))
        self.tablaTemp = tvInstrucciones
        
        
        # tvInstrucciones.delete(*tvInstrucciones.get_children())
        # tvInstrucciones.delete(*tvInstrucciones.get_children())
        tvInstrucciones.column("#0",width=90)
        tvInstrucciones.column("colInstrucciones",width=90,anchor=CENTER)
        self.existeTabla = True
        
        tvInstrucciones.heading("#0",text="Dron",anchor=CENTER)
        tvInstrucciones.heading("colInstrucciones", text="Valor", anchor=CENTER)
        
        lb = tk.Label(listaMensajes_frame,text="Lista Instrucciones",font=('Bold',20))
        for i, instruccion in enumerate(listaInstrucciones):
            tvInstrucciones.insert("", "end", text=(instruccion.CInstrucciones.dron_actual), values=(instruccion.CInstrucciones.posicion))
        
        
        lb.pack()
        tvInstrucciones.pack()
        tvInstrucciones.pack(side="left") 
        listaMensajes_frame.pack(pady=20)
        
    
    def mostrar_tablaMensajes(self):
        self.clear_page()
        tablaMensajes_frame = tk.Frame(self.main_frame)
        tvMensajes = ttk.Treeview(tablaMensajes_frame,columns=("colMensajes"))
        tvMensajes.column("#0",width=90)
        tvMensajes.column("colMensajes",width=90,anchor=CENTER)
        
        tvMensajes.heading("#0",text="Nombre",anchor=CENTER)
        tvMensajes.heading("colMensajes", text="Sistema", anchor=CENTER)
        
        lb = tk.Label(tablaMensajes_frame,text="Lista de Mensajes",font=('Bold',20))
        listado_mensajes = self.readFile.get_listaMensajes()
        
        for i, mensaje in enumerate(listado_mensajes):
            tvMensajes.insert("", "end", text=(mensaje.CMensajes.nombre_mensaje), values=(mensaje.CMensajes.sistema_drones))
        
        def item_selected(event):
            for selected_item in tvMensajes.selection():
                item = tvMensajes.item(selected_item)
                # print(item)
                nombreMensaje = item['text']
                valuesList = item['values']
                if valuesList:
                    sistema = valuesList[0]
                    print(sistema)

                    listaImstrucciones = listado_mensajes.encontrar_sistema(sistema)
                    
                    self.mostrar_instrucciones(listaImstrucciones,sistema,nombreMensaje)
                
        tvMensajes.bind('<<TreeviewSelect>>',item_selected)
        
        
        lb.pack()
        tvMensajes.pack(pady=(10, 0))  # Ajusta pady
        tablaMensajes_frame.pack(pady=20)
        # lb.pack()
        # tvMensajes.pack()
        # tvMensajes.pack(side="left") 
        # tablaMensajes_frame.pack(pady=20)
    
    
    def mostrar_instrucciones(self, listaInstrucciones,sistema,nombreMensaje):
        self.tiempoTemp = 0
        tablaMensajes_frame = tk.Frame(self.main_frame)
        tvInstrucciones = ttk.Treeview(tablaMensajes_frame, columns=( "Valor", "Mensaje", "Tiempo"))
        
        tvInstrucciones.column("#0", width=90)
        tvInstrucciones.column("Valor", width=90, anchor=tk.CENTER)
        tvInstrucciones.column("Mensaje", width=90, anchor=tk.CENTER)
        tvInstrucciones.column("Tiempo", width=90, anchor=tk.CENTER)
        
        tvInstrucciones.heading("#0", text="Dron", anchor=tk.CENTER)
        tvInstrucciones.heading("Valor", text="Valor", anchor=tk.CENTER)
        tvInstrucciones.heading("Mensaje", text="Mensaje", anchor=tk.CENTER)
        tvInstrucciones.heading("Tiempo", text="Tiempo", anchor=tk.CENTER)
        
        lb = tk.Label(tablaMensajes_frame, text="Instrucciones", font=('Bold', 16))
        listado_sistemasDrones = self.readFile.get_listaSistemasDrones()
        listado_contenido = listado_sistemasDrones.encontrar_listaContenido(sistema)
        
        mensaje_completo = ""
        for instruccion in listaInstrucciones:
            dron_temp = instruccion.CInstrucciones.dron_actual
            lista_alturas = listado_contenido.get_listaAlturas(dron_temp)
            altura_temp = instruccion.CInstrucciones.posicion

            letra_temp = lista_alturas.encontrar_letra(altura_temp)
            mensaje_completo += letra_temp
            # self.tiempoTemp=0
            tiempoOptimo = self.calcular_tiempo(int(altura_temp),dron_temp)
            

            tvInstrucciones.insert("", "end", text=instruccion.CInstrucciones.dron_actual, values=(instruccion.CInstrucciones.posicion, letra_temp, tiempoOptimo))
    
        self.lista_mensajeCreado_temp.insertar(CMensajeCreado(nombreMensaje,sistema,mensaje_completo,tiempoOptimo))
        lbMensaje = tk.Label(tablaMensajes_frame, text="Mensaje decifrado: " + mensaje_completo, font=('Bold', 12))
        lbTiempoOptimo = tk.Label(tablaMensajes_frame, text="Tiempo Optimo: " + str(tiempoOptimo), font=('Bold', 12))
        # self.lista_mensajeCreado_temp.imprimir()
        
        lb.pack()
        tvInstrucciones.pack()
        tvInstrucciones.pack(side="left")
        lbMensaje.pack()
        lbTiempoOptimo.pack()
        tablaMensajes_frame.pack(pady=20)
        
        
    # def calcular_tiempo(self, alturaTemp, dron_temp):
    #     while self.tiempoTemp < alturaTemp:
    #         print(dron_temp + " subió")
    #         self.tiempoTemp += 1
    #     while self.tiempoTemp > alturaTemp:
    #         print(dron_temp + " bajó")
    #         self.tiempoTemp -= 1
    #     print(dron_temp + " emitio Luz")
        
    #     # Agregar un bucle de espera hasta que el dron alcance su objetivo
    #     while self.tiempoTemp == alturaTemp:
    #         print(dron_temp + " esperando")


        
    # def calcular_tiempo(self,alturaTemp,dron_temp):
    #     isOff = True
    #     self.tiempoTemp =+1
        
    #     if alturaTemp >= self.tiempoTemp:
    #         self.tiempoTemp += 1
    #         print("El dron: " + dron_temp + " subio")
    #     elif str(self.tiempoTemp) in self.cadenaTiempo:
    #         self.tiempoTemp += 1
    #         print("Esperar")
    #     else: 
    #         self.tiempoTemp = alturaTemp + 1
    #         self.tiempoTemp += 1
    #         print("El dron: " + dron_temp + " bajo")
        
    #     print("L" + str(alturaTemp))
        
    
    def calcular_tiempo(self, alturaTemp, dron_temp):
        if alturaTemp >= self.tiempoTemp:
            self.tiempoTemp = alturaTemp + 1
            print("El dron: " + dron_temp + " subio")
            
        elif alturaTemp <= self.tiempoTemp:
            self.tiempoTemp += 1
            print("Esperar, tiempo encontrado")
        elif str(self.tiempoTemp) in self.cadenaTiempo: 
            # self.tiempoTemp = alturaTemp + 1
            self.tiempoTemp += 1
            print("El dron: " + dron_temp + " bajo")

        tiempo_original = self.tiempoTemp

        tiempoAsString = str(self.tiempoTemp)
        self.cadenaTiempo += tiempoAsString

        # if self.tiempoTemp != tiempo_original:
        #     print("Tiempo Encontrado")

        print("El dron: " + dron_temp, "enciende luz: " + tiempoAsString)
        print("Tiempo optimo: " + str(self.tiempoTemp))
        return self.tiempoTemp
    
    # def calcular_tiempo(self, alturaTemp, dron_temp):
    #     self.tiempoTemp = 0
        
        
        
    #     while self.tiempoTemp < alturaTemp:
    #         self.tiempoTemp += 1
    #         print("El dron: " + dron_temp, "sube")

        

    #     if self.tiempoTemp == alturaTemp:
    #         self.tiempoTemp += 1
    #         if str(self.tiempoTemp) in self.cadenaTiempo:
    #             while str(self.tiempoTemp) in self.cadenaTiempo:
    #                 self.tiempoTemp += 1
    #                 print("El dron: " + dron_temp, "esperando")
            
    #         print("El dron: " + dron_temp, "emite luz en:", self.tiempoTemp)
    #         tiempoAsString = str(self.tiempoTemp)
    #         self.cadenaTiempo += tiempoAsString
    #         self.ultimaAltura = self.tiempoTemp

    #     # while str(self.tiempoTemp) in self.cadenaTiempo:
    #     #     self.tiempoTemp += 1
    #     #     print("El dron: " + dron_temp, "esperando")

    #     return self.tiempoTemp


    
    
    def inicializar(self):
        self.readFile.borrarListas()
        messagebox.showinfo("Inicializar", "Se reinicio el programa correctamente")
    
    def crear_xml_salida(self):
        self.lista_mensajeCreado_temp.generar_xml(self.lista_mensajeCreado_temp)
        messagebox.showinfo("xml salida", "Se genero archivo xml")
    
    def graficar_lista_drones(self):
        self.readFile.graficar()
        messagebox.showinfo("Grafica", "Grafica creada")
    
    def clear_page(self):
        for frame in self.main_frame.winfo_children():
            frame.destroy()
    
    def cargar_archivo(self):
        self.clear_page()
        cargar_frame = tk.Frame(self.main_frame)
        lb = tk.Label(cargar_frame,text="Cargar Archivo",font=('Bold',20))
        lb.pack()
        cargar_frame.pack(pady=20)
        file_path = filedialog.askopenfilename(filetypes=[("Archivos", "*.xml")])
        self.file_path = file_path 
        if file_path:
            # reader = readFile()
            self.readFile.cargarXml(file_path)
            messagebox.showinfo("cargar Archivo", "Archivo cargado exitosamente.")
    
    def ayuda(self):
        self.clear_page()
        ayuda_frame = tk.Frame(self.main_frame)
        lb = tk.Label(ayuda_frame,text="Ayuda\n",font=('Bold',20))
        lb2 = tk.Label(ayuda_frame,text="Nombre: Helen Janet Rodas Castro \n Carnet: 202200066 \n Curso:IPC 2 \n Seccion: D \n Semestre: 4to. Semestre\n",font=('italic',14))
        link = tk.Label(ayuda_frame,text="Link: Pronto...",font=('italic',14))
        lb.pack()
        lb2.pack()
        link.pack()
        ayuda_frame.pack(pady=20)

    def reiniciar_tabla(self,table):
        for item in table.get_children():
            table.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('900x500')

    root.resizable(False, False)
    frm = FrmInicio(root)
    root.mainloop()
    