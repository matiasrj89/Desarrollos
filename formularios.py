from tkinter import *
import modulo_bd
import globales
import validacion
from tkinter import messagebox
from tkinter.messagebox import *
import modulo_grilla as mdgrilla
from modulo_bd import *
from tkinter import ttk
from tkcalendar import DateEntry
import hashlib
import random
import string


#####################################################################
###################Formularios  REGISTROS############################
#####################################################################

######################Formulario Baja_registros##################################

class FormBaja_registro():
    """
    Clase utilizada para la generacion de 
    un formulario de baja.
    """

    def __init__(self):
        """
        Inicializacion de formulario baja
        """

        def on_closing(self):
                """
                Detecta cuando se cierra la ventana
                de formulario de baja
                """
                self.__closing=True
                self.__master.destroy()

        self.__closing=False

        self.__master =  Toplevel()

        self.__master.protocol("WM_DELETE_WINDOW", lambda :on_closing(self))
        self.__master.configure(bg="gray")

        ## Creacion de header
        self.__header_frame = Frame(self.__master, bg="gray", 
                                    bd=5, height=20, relief=FLAT)

        # Elements of header Frame
        self.__header = Label(
            self.__header_frame,
            text="Formulario de Baja",
            foreground="white",
            bg="gray",
            font=("calibri", 15),
        )
        self.__header.grid(row=0, column=0)
        self.__header_frame.pack(fill=X)


        #### Container Frame
        self.__container = Frame(self.__master, bg="cyan", 
                                bd=5, relief=SUNKEN)




        self.__lbl_descripcion = Label(self.__container,text='Descripcion:',
                             font=("calibri", 15)  ,bg="cyan")
        
        self.__lbl_descripcion.grid(row=0, column=0)

        self.__entry_descripcion = Entry(self.__container, textvariable='hola',
                                font=("calibri", 15))
        
        self.__entry_descripcion.grid(row=0, column=1)
        self.__entry_descripcion.bind('<KeyRelease>', self.checkkey)


        self.__lbl_lista_registros=Label(self.__container,text='Lista:',
                             font=("calibri", 15) ,bg="cyan" )
        self.__lbl_lista_registros.grid(row=0, column=2)

        self.__list_lista_registros= Listbox(self.__container)
        self.__list_lista_registros.grid(row=1, column=2, rowspan=4)
        self.__list_lista_registros.bind('<<ListboxSelect>>', self.clicklist)


        self.__lbl_ID_header = Label (self.__container,text='ID :', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_ID_header.grid(row=1, column=0)

        self.__lbl_ID = Label (self.__container,text='#ID ', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_ID.grid(row=1, column=1)

        self.__lbl_lote_partida_header = Label(self.__container,text='lote_partida:', 
                                    bg="cyan", font=("calibri", 15)  )
        self.__lbl_lote_partida_header.grid(row=2, column=0)

        self.__lbl_lote_partida =  Label(self.__container, 
                                bg="cyan", font=("calibri", 15))
        self.__lbl_lote_partida.grid(row=2, column=1)

        self.__lbl_vencimiento_header = Label (self.__container,text='vencimiento:', 
                                        bg="cyan", font=("calibri", 15)  )
        self.__lbl_vencimiento_header.grid(row=3, column=0)



        self.__lbl_vencimiento = Label(self.__container, 
                                bg="cyan",font=("calibri", 15))
        self.__lbl_vencimiento.grid(row=3, column=1)

        self.__lbl_cantidadheader = Label(self.__container,text='cantidad:', 
                                        bg="cyan", font=("calibri", 15)  )
        self.__lbl_cantidadheader.grid(row=4, column=0)

        self.__lbl_cantidad = Label(self.__container, bg="cyan", 
                                    font=("calibri", 15))
        self.__lbl_cantidad.grid(row=4, column=1)



        self.__btn_aceptar = Button(self.__container, text="Aceptar",  
                                  font=("calibri", 15), command=lambda :aceptar(self))
        self.__btn_aceptar.grid(row=6, column=0)

        self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                    font=("calibri", 15), command= lambda :cancelar(self))
        self.__btn_cancelar.grid(row=6, column=1)

        self.__container.pack(fill=BOTH)

         ##################### Cargo lista a la lista descripcion###########################
        self.__lista_registros=[]
        lista_descripcion=[]
        self.__lista_registros = modulo_bd.buscar_registros_all()
        
        for registro in self.__lista_registros:
            
            fila = str(registro.registro_id)+ ' - '  +str(registro.insumo_id.descripcion)  
            print(fila)
            lista_descripcion.append(fila )
     
        for item in lista_descripcion:
            self.__list_lista_registros.insert('end',item) 



        ######################  Aceptar/Cancelar  #######################################
        def aceptar(self):
            """
            Genera alta en BD
            """
            
            ID = self.__lbl_ID['text']
            modulo_bd.eliminar_registro(ID)

            self.__lbl_ID['text']= ''
            self.__lbl_lote_partida['text']=''
            self.__lbl_cantidad['text']=''
            self.__lbl_vencimiento['text']=''

            self.__master.destroy()
            

        def cancelar(self):
            """
            Cierra ventana de baja
            """
            globales.formBajaShowing=False
            self.__deleted=False
            self.__master.destroy()

        self.__master.grab_set()
        self.__master.focus_force()
        self.__master.wait_window()


    def isclosing(self):
        return (self.__closing)   

    def checkkey(self,event):
        value=event.widget.get() 
        
        lista_descripcion=[]
        if value != '': 
            for item in self.__lista_registros: 
                if str(value).lower() in str(item.insumo_id.descripcion).lower():
                    fila =str( item.registro_id)+' - '+str(item.insumo_id.descripcion)
                    lista_descripcion.append(fila) 

        else: 
            for item in self.__lista_registros: 
                fila =str( item.registro_id)+' - '+str(item.insumo_id.descripcion)
                lista_descripcion.append(fila)        
        
        self.__lbl_ID['text']= ''
        self.__lbl_lote_partida['text']=''
        self.__lbl_cantidad['text']=''
        self.__lbl_vencimiento['text']=''
        
        self.__list_lista_registros.delete(0, 'end') 
        for item in lista_descripcion:
            self.__list_lista_registros.insert('end',item)


    def clicklist(self,event):
        selected=event.widget.get(ANCHOR)
        lista_split = selected.split(sep='-', maxsplit=1)

        registro_id=lista_split[0]
        registro_id=registro_id.replace(" ", "")

        descripcion_registro= lista_split[1]
        descripcion_registro=descripcion_registro.replace(" ", "")
        self.__entry_descripcion.delete(0,END)
        self.__entry_descripcion.insert(0,descripcion_registro)

        registro = modulo_bd.buscar_registro(registro_id)
        
        self.__lbl_ID['text']= registro[0].registro_id
        self.__lbl_lote_partida['text']=registro[0].lote_partida
        self.__lbl_cantidad['text']=registro[0].cantidad
        self.__lbl_vencimiento['text']=registro[0].vencimiento       
######################Formulario Alta_registros##################################

class FormAlta_registro():
    """
    Clase utilizada para la generacion de 
    un formulario de alta.
    """
    def __init__(self):
        """
        Inicializacion de formulario alta
        """

        def on_closing(self):
                """
                Detecta cuando se cierra la ventana
                de formulario de alta
                """
                self.__closing=True
                self.__master.destroy()

        self.__closing=False

        self.__master =  Toplevel()

        self.__master.protocol("WM_DELETE_WINDOW", lambda :on_closing(self))
        self.__master.configure(bg="gray")

        ## Creacion de header
        self.__header_frame = Frame(self.__master, bg="gray", bd=5, height=20, relief=FLAT)

        # Elements of header Frame
        self.__header = Label(
            self.__header_frame,
            text="Formulario de Alta",
            foreground="white",
            bg="gray",
            font=("calibri", 15),
        )
        self.__header.grid(row=0, column=0)
        self.__header_frame.pack(fill=X)


        #### Container Frame
        self.__container = Frame(self.__master, bg="cyan", bd=5, relief=SUNKEN)

        self.__lbl_insumo = Label (self.__container,text='Codigo Insumo:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_insumo.grid(row=0, column=0)



        self.__entry_codigo_unico_insumo = ttk.Combobox(self.__container, font=("calibri", 15), name='combo_codigo')
        self.__entry_codigo_unico_insumo.bind('<KeyRelease>', self.checkkey)
        self.__entry_codigo_unico_insumo.grid(row=0, column=1)

        self.__lbl_lista = Label (self.__container,text='Lista de insumos:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_lista.grid(row=0, column=2) 


        self.__list_lista_insumos = Listbox (self.__container, 
                        bg="cyan", font=("calibri", 15)  )
        self.__list_lista_insumos.grid(row=1, column=2, rowspan=4)
        self.__list_lista_insumos.bind('<<ListboxSelect>>', self.clicklist)

        self.__lbl_descripcion = Label (self.__container,text='Descripcion:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_descripcion.grid(row=1, column=0)

        self.__entry_descripcion = ttk.Combobox(self.__container, font=("calibri", 15),name='combo_descripcion')
        self.__entry_descripcion.bind('<KeyRelease>', self.checkkey)
        self.__entry_descripcion.grid(row=1, column=1)

        self.__lbl_lote_partida = Label(self.__container,text='Lote/Partida:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_lote_partida.grid(row=2, column=0)

        self.__entry_lote_partida = Entry(self.__container, font=("calibri", 15))
        self.__entry_lote_partida.grid(row=2, column=1)

        self.__lbl_vencimiento = Label(self.__container,text='Vencimiento:', 
                                bg="cyan", font=("calibri", 15) )
        self.__lbl_vencimiento.grid(row=3, column=0)

        # self.__entry_vencimiento = Entry(self.__container, font=("calibri", 15))
        self.__entry_vencimiento= DateEntry(self.__container, width=12, year=2019, month=6, day=22, 
                                            background='darkblue', foreground='white', borderwidth=2, state='readonly')
        self.__entry_vencimiento.grid(row=3, column=1)





        self.__lbl_cantidad = Label (self.__container,text='Cantidad:', 
                                    bg="cyan", font=("calibri", 15)  )
        self.__lbl_cantidad.grid(row=4, column=0)

        self.__entry_cantidad = Entry(self.__container, font=("calibri", 15))
        self.__entry_cantidad.grid(row=4, column=1)

        self.__btn_aceptar = Button(self.__container, text="Aceptar", 
                                    font=("calibri", 15), command=lambda :aceptar(self))
        self.__btn_aceptar.grid(row=5, column=0)

        self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                    font=("calibri", 15), command= lambda :cancelar(self))
        self.__btn_cancelar.grid(row=5, column=1)

        self.__container.pack(fill=BOTH)



        ##################### Cargo lista a la lista descripcion###########################
        self.__lista_insumos=[]
        lista_descripcion=[]
        self.__lista_insumos = modulo_bd.buscar_insumo_all()
        
        for insumo in self.__lista_insumos:
            if insumo.activo: # Cargo solo los activos
                fila = str(insumo.codigo_unico)+ ' - '  +str(insumo.descripcion)  
                print(fila)
                lista_descripcion.append(fila )
     
        for item in lista_descripcion:
            self.__list_lista_insumos.insert('end',item)  


        ##################### Cargo lista al combo descripcion y codigo###########################
        self.__lista_insumos=[]
        lista_desc=[]
        lista_codigo=[]
        self.__lista_insumos = modulo_bd.buscar_insumo_all()
        
        for insumo in self.__lista_insumos:
            if insumo.activo: # Cargo solo los activos
                lista_desc.append(insumo.descripcion)
                lista_codigo.append(insumo.codigo_unico)
     
        self.__entry_descripcion['values']=  lista_desc
        self.__entry_codigo_unico_insumo['values']=  lista_codigo


        ######################  Aceptar/Cancelar  #######################################
        def aceptar(self):
            """
            Genera alta en la BD
            """
            codigo_insumo = self.__entry_codigo_unico_insumo.get()
            vencimiento = self.__entry_vencimiento.get()       
            lote_partida = self.__entry_lote_partida.get()
            cantidad = self.__entry_cantidad.get()



            if (validacion.validacion('abc')): # Esto dara siempre verdadero, adaptar.
                if (validacion.validacion_numerica(cantidad)):
                    modulo_bd.alta_registro( codigo_insumo = codigo_insumo, 
                                    lote_partida = lote_partida, 
                                    vencimiento = vencimiento,
                                    cantidad = cantidad)
                    self.__master.destroy()    
                else:
                        showinfo('Error ',  
                                'Por favor, ingrese un valor numerico en cantidad')
            else:
                showinfo('Error',
                        'Titulo no cumple con el formato permitido de ingreso')   
            

        def cancelar(self):
            """
            Cierra ventana de  alta
            """

            self.__master.destroy()

        self.__master.grab_set()
        self.__master.focus_force()
        self.__master.wait_window()    



    def isclosing(self):
        return (self.__closing)   
    
    def checkkey(self,event):
            caller = event.widget
            value = event.widget.get() 
            print(value) 

            if 'combo_descripcion' in str(caller):
                self.__entry_codigo_unico_insumo.set('')
                lista_descripcion=[]
                lista_codigo=[]
                # get data from l 
                if value != '': 
                    for item in self.__lista_insumos: 
                        if item.activo: # Cargo solo los activos
                            if value.lower() in item.descripcion.lower(): 
                                lista_descripcion.append(item.descripcion) 
                                lista_codigo.append(item.codigo_unico)
                else:
                    for item in self.__lista_insumos: 
                        if item.activo: # Cargo solo los activos
                            lista_descripcion.append(item.descripcion)
                            lista_codigo.append(item.codigo_unico) 


            elif 'combo_codigo' in str(caller):
                self.__entry_descripcion.set('')
                lista_descripcion=[]
                lista_codigo=[]
                # get data from l 
                if value != '': 
                    for item in self.__lista_insumos: 
                        if item.activo: # Cargo solo los activos
                            if str(value).lower() in str(item.codigo_unico).lower(): 
                                lista_codigo.append(item.codigo_unico)
                                lista_descripcion.append(item.descripcion) 
                else:
                    for item in self.__lista_insumos: 
                        if item.activo: # Cargo solo los activos
                            lista_descripcion.append(item.descripcion)
                            lista_codigo.append(item.codigo_unico)

            
            
            
            self.__entry_descripcion['values']= lista_descripcion
            self.__entry_codigo_unico_insumo['values']= lista_codigo

            # Recargo lista con nva seleccion
            self.__list_lista_insumos.delete(0, 'end') 
            index=0
            for item in lista_codigo:
                fila = str(item)+' - '+ str(lista_descripcion[index])
                self.__list_lista_insumos.insert('end',fila)
                index+=1






        # value=event.widget.get() 
        
        # lista_descripcion=[]
        # if value != '': 
        #     for item in self.__lista_registros: 
        #         if str(value).lower() in str(item.insumo_id.descripcion).lower():
        #             fila =str( item.registro_id)+' - '+str(item.insumo_id.descripcion)
        #             lista_descripcion.append(fila) 

        # else: 
        #     for item in self.__lista_registros: 
        #         fila =str( item.registro_id)+' - '+str(item.insumo_id.descripcion)
        #         lista_descripcion.append(fila)        
        
        # self.__lbl_ID_['text']= ''
        # self.__lbl_lote_partida['text']=''
        # self.__lbl_cantidad['text']=''
        # self.__lbl_vencimiento['text']=''
        
        # self.__list_lista_registros.delete(0, 'end') 
        # for item in lista_descripcion:
        #     self.__list_lista_registros.insert('end',item)














    def clicklist(self,event):
        selected=event.widget.get(ANCHOR)
        lista_split = selected.split(sep='-', maxsplit=1)

        insumo_codigo_unico=lista_split[0]
        insumo_codigo_unico=insumo_codigo_unico.replace(" ", "")

        descripcion_insumo= lista_split[1]
        descripcion_insumo=descripcion_insumo.replace(" ", "")
        self.__entry_descripcion.delete(0,END)
        self.__entry_descripcion.insert(0,descripcion_insumo)

        self.__entry_codigo_unico_insumo.delete(0,END)
        self.__entry_codigo_unico_insumo.insert(0,insumo_codigo_unico)

       
 
        
######################Formulario Buscar_registros#################################

class FormBuscar_registro():
    """
    Clase utilizada para la generacion de 
    un formulario de busqueda.
    """
    def __init__(self):
        """
        Inicializacion de formulario de busqueda
        """

        def on_closing(self):
                """
                Detecta cuando se cierra la ventana
                de formulario de busqueda
                """
                self.__closing=True
                self.__master.destroy()

        self.__closing=False

        self.__master =  Toplevel()
  
        self.__master.protocol("WM_DELETE_WINDOW", lambda :on_closing(self))
        self.__master.configure(bg="gray")

        ## Creacion de header
        self.__header_frame = Frame(self.__master, bg="gray", bd=5, 
                                    height=20, relief=FLAT)

        # Elements of header Frame
        self.__header = Label(
            self.__header_frame,
            text="Formulario de Busqueda",
            foreground="white",
            bg="gray",
            font=("calibri", 15),
        )
        self.__header.grid(row=0, column=0)
        self.__header_frame.pack(fill=X)


        #### Container Frame
        self.__container = Frame(self.__master, bg="cyan", bd=5, relief=SUNKEN)

        self.__lbl_descripcionheader = Label(self.__container,text='Descripcion:', 
                                            bg="cyan", font=("calibri", 15)  )
        self.__lbl_descripcionheader.grid(row=0, column=0)


        self.__entry_descripcion = Entry(self.__container)
        self.__entry_descripcion.grid(row=0, column=1)
        self.__entry_descripcion.bind('<KeyRelease>', self.checkkey)


        self.__lbl_lista = Label (self.__container,text='Lista de Registros :', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_lista.grid(row=0, column=2)

        self.__list_lista_registros = Listbox (self.__container, 
                        bg="cyan", font=("calibri", 15)  )
        self.__list_lista_registros.grid(row=1, column=2, rowspan=4)
        self.__list_lista_registros.bind('<<ListboxSelect>>', self.clicklist)


        
        self.__lbl_ID_header = Label (self.__container,text='ID :', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_ID_header.grid(row=1, column=0)

        self.__lbl_ID_ = Label (self.__container,text='#ID ', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_ID_.grid(row=1, column=1)

        self.__lbl_lote_partida_header = Label(self.__container,text='lote_partida:', 
                                    bg="cyan", font=("calibri", 15)  )
        self.__lbl_lote_partida_header.grid(row=2, column=0)

        self.__lbl_lote_partida =  Label(self.__container, 
                                bg="cyan", font=("calibri", 15))
        self.__lbl_lote_partida.grid(row=2, column=1)

        self.__lbl_vencimiento_header = Label (self.__container,text='vencimiento:', 
                                        bg="cyan", font=("calibri", 15)  )
        self.__lbl_vencimiento_header.grid(row=3, column=0)

        self.__lbl_vencimiento = Label(self.__container, 
                                bg="cyan",font=("calibri", 15))
        self.__lbl_vencimiento.grid(row=3, column=1)

        self.__lbl_cantidadheader = Label(self.__container,text='cantidad:', 
                                        bg="cyan", font=("calibri", 15)  )
        self.__lbl_cantidadheader.grid(row=4, column=0)

        self.__lbl_cantidad = Label(self.__container, bg="cyan", 
                                    font=("calibri", 15))
        self.__lbl_cantidad.grid(row=4, column=1)

        self.__btn_aceptar = Button(self.__container, text="Buscar",  
                                    font=("calibri", 15), command=lambda :aceptar(self))
        self.__btn_aceptar.grid(row=5, column=0)

        self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                    font=("calibri", 15), command= lambda :cancelar(self))
        
        self.__btn_cancelar.grid(row=5, column=1)

        self.__container.pack(fill=BOTH)

         ##################### Cargo lista a la lista descripcion###########################
        self.__lista_registros=[]
        lista_descripcion=[]
        self.__lista_registros = modulo_bd.buscar_registros_all()
        
        for registro in self.__lista_registros:
            
            fila = str(registro.registro_id)+ ' - '  +str(registro.insumo_id.descripcion)  
            print(fila)
            lista_descripcion.append(fila )
     
        for item in lista_descripcion:
            self.__list_lista_registros.insert('end',item)      


        ######################  Aceptar/Cancelar  #######################################
        def aceptar(self):
            """
            limpio campos
            """
            self.__lbl_descripcion['text']= ''
            self.__lbl_lote_partida['text']= ''
            self.__lbl_vencimiento['text']=''
            self.__lbl_cantidad['text']=''
            
            """
            Realiza busqeda en BD
            """
            ID = self.__entry_ID.get() 
            if (validacion.validacion_numerica(ID)):
                row = modulo_bd.buscar_registro(ID)  
                row = tuple(row)
                for x in row:
                    
                    self.__lbl_descripcion['text']= x.descripcion
                    self.__lbl_lote_partida['text']= x.lote_partida
                    self.__lbl_vencimiento['text']= x.vencimiento
                    self.__lbl_cantidad['text']= x.cantidad
            else:
                showinfo('Error en ID',
                        'Por favor, ingrese un valor numerico en ID')

        def cancelar(self):
            """
            Cierra ventana de busqueda
            """
            globales.formBajaShowing=False

            self.__master.destroy()
        
        self.__master.grab_set()
        self.__master.focus_force()
        self.__master.wait_window()    


    def isclosing(self):
        return (self.__closing)   

    def checkkey(self,event):
        value=event.widget.get() 
        
        lista_descripcion=[]
        if value != '': 
            for item in self.__lista_registros: 
                if str(value).lower() in str(item.insumo_id.descripcion).lower():
                    fila =str( item.registro_id)+' - '+str(item.insumo_id.descripcion)
                    lista_descripcion.append(fila) 

        else: 
            for item in self.__lista_registros: 
                fila =str( item.registro_id)+' - '+str(item.insumo_id.descripcion)
                lista_descripcion.append(fila)        
        
        self.__lbl_ID_['text']= ''
        self.__lbl_lote_partida['text']=''
        self.__lbl_cantidad['text']=''
        self.__lbl_vencimiento['text']=''
        
        self.__list_lista_registros.delete(0, 'end') 
        for item in lista_descripcion:
            self.__list_lista_registros.insert('end',item)


    def clicklist(self,event):
        selected=event.widget.get(ANCHOR)
        lista_split = selected.split(sep='-', maxsplit=1)

        registro_id=lista_split[0]
        registro_id=registro_id.replace(" ", "")

        descripcion_registro= lista_split[1]
        descripcion_registro=descripcion_registro.replace(" ", "")
        self.__entry_descripcion.delete(0,END)
        self.__entry_descripcion.insert(0,descripcion_registro)

        registro = modulo_bd.buscar_registro(registro_id)
        
        self.__lbl_ID_['text']= registro[0].registro_id
        self.__lbl_lote_partida['text']=registro[0].lote_partida
        self.__lbl_cantidad['text']=registro[0].cantidad
        self.__lbl_vencimiento['text']=registro[0].vencimiento

######################Formulario Modificar_registrosr##############################

class FormModificar_registro():


    """
    Clase utilizada para la generacion de 
    un formulario de modificacion.
    """
    def __init__(self,*args):
        """
        Inicializacion de formulario de modificacion
        """
        self.__ID = str(args[0][0])
        

        def on_closing(self):
                """
                Detecta cuando se cierra la ventana
                de formulario de modificacion
                """
                self.__closing=True
                self.__master.destroy()

        self.__closing=False

        self.__master =  Toplevel()
        self.__master.protocol("WM_DELETE_WINDOW", lambda :on_closing(self))
        self.__master.configure(bg="gray")

        ## Creacion de header
        self.__header_frame = Frame(self.__master, bg="gray", 
                                    bd=5, height=20, relief=FLAT)

        # Elements of header Frame
        self.__header = Label(
            self.__header_frame,
            text="Formulario de Modificacion",
            foreground="white",
            bg="gray",
            font=("calibri", 15),
        )
        self.__header.grid(row=0, column=0)
        self.__header_frame.pack(fill=X)


        #### Container Frame
        self.__container = Frame(self.__master, bg="cyan", bd=5, relief=SUNKEN)
        

        self.__lbl_descripcion = Label (self.__container,text='descripcion:', 
                                        bg="cyan", font=("calibri", 15)  )
        self.__lbl_descripcion.grid(row=0, column=0)



        self.__entry_descripcion = ttk.Combobox(self.__container, font=("calibri", 15))
        self.__entry_descripcion.bind('<KeyRelease>', self.checkkey)
        self.__entry_descripcion.grid(row=0, column=1)

        self.__lbl_lista  = Label (self.__container,text='Lista:', 
                                        bg="cyan", font=("calibri", 15)  )
        self.__lbl_lista.grid(row=0, column=2) 

        self.__list_lista_insumos= Listbox (self.__container, 
                        bg="cyan", font=("calibri", 15)  )
        self.__list_lista_insumos.grid(row=1, column=2, rowspan=4)
        self.__list_lista_insumos.bind('<<ListboxSelect>>', self.clicklist)

        self.__lbl_codigo_insumo_header = Label (self.__container,text='Codigo Insumo:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_codigo_insumo_header.grid(row=1, column=0)

        self.__lbl_codigo_insumo = Label(self.__container, font=("calibri", 15), text='#Cod. Insumo',
                                bg="cyan")
        self.__lbl_codigo_insumo.grid(row=1, column=1)


        self.__lbl_lote_partida = Label (self.__container,text='Lote/Partida:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_lote_partida.grid(row=2, column=0)

        self.__entry_lote_partida = Entry(self.__container, font=("calibri", 15))
        self.__entry_lote_partida.grid(row=2, column=1)
        self.__entry_lote_partida.insert(0,str(args[0][2]))

        self.__lbl_vencimiento = Label (self.__container,text='Vencimiento:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_vencimiento.grid(row=3, column=0)

        self.__entry_vencimiento = Entry(self.__container, font=("calibri", 15))
        self.__entry_vencimiento.grid(row=3, column=1)
        self.__entry_vencimiento.insert(0,str(args[0][3]))


        self.__lbl_cantidad = Label (self.__container,text='cantidad:', 
                                    bg="cyan", font=("calibri", 15)  )
        
        self.__lbl_cantidad.grid(row=4, column=0)

        self.__entry_cantidad = Entry(self.__container, 
                                    font=("calibri", 15))
        
        self.__entry_cantidad.grid(row=4, column=1)
        
        self.__entry_cantidad.insert(0,str(args[0][4]))

        self.__btn_aceptar = Button(self.__container, text="Aceptar",  
                                    font=("calibri", 15), command=lambda :aceptar(self))
        self.__btn_aceptar.grid(row=5, column=0)

        self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                    font=("calibri", 15), command= lambda :cancelar(self))
        self.__btn_cancelar.grid(row=5, column=1)

        self.__container.pack(fill=BOTH)
       

        ##################### Cargo lista al combo descripcion###########################
        self.__lista_insumos=[]
        lista_descripcion=[]
        lista_codigo=[]
        self.__lista_insumos = modulo_bd.buscar_insumo_all()
        
        for insumo in self.__lista_insumos:
            if insumo.activo: # Cargo solo los activos
                lista_descripcion.append(insumo.descripcion)
                lista_codigo.append(insumo.codigo_unico)
     
        self.__entry_descripcion['values']=  lista_descripcion

        # Recargo lista con nva seleccion
        self.__list_lista_insumos.delete(0, 'end') 
        index=0
        for item in lista_codigo:
            fila = str(item)+' - '+ str(lista_descripcion[index])
            self.__list_lista_insumos.insert('end',fila)
            index+=1  

        ######################  Aceptar/Cancelar  #######################################
        def aceptar(self):
            """
            Genera modificacion en BD
            """
            id= self.__ID
            codigo_insumo = self.__lbl_codigo_insumo['text']
            lote_partida = self.__entry_lote_partida.get()
            vencimiento = self.__entry_vencimiento.get()
            cantidad = self.__entry_cantidad.get() 

            print("Valores a modificar")
            print(id +' '+ str(lote_partida)+' ' + str(vencimiento)+' '+ str(cantidad) +' '+ str(codigo_insumo) )

            if (validacion.validacion('abc')): #Validacion no usada en este caso
                if (validacion.validacion_numerica(cantidad)):
                    modulo_bd.modificar_registro(id=id,
                                        codigo_insumo = codigo_insumo,
                                        lote_partida=lote_partida,
                                        vencimiento=vencimiento,
                                        cantidad=cantidad)
                    self.__master.destroy()
                    
                else:
                    showinfo('Error de formato','Por favor, ingrese un valor'
                            ' numerico en cantidad')
            else:
                showinfo('Error de Formato','titulo no cumple con el' 
                        'formato permitido de ingreso')
         

        def cancelar(self):
            """
            Cierra ventana de modificacion
            """
            globales.formBajaShowing=False
  
            self.__master.destroy()

        self.__master.grab_set()
        self.__master.focus_force()
        self.__master.wait_window()  


    def isclosing(self):
        return (self.__closing)   


    def checkkey(self,event):
            value = event.widget.get() 
            print(value) 
            lista_descripcion=[]
            lista_codigo=[]
            # get data from l 
            if value != '': 
                for item in self.__lista_insumos: 
                    if item.activo: # Cargo solo los activos
                        if value.lower() in item.descripcion.lower(): 
                            lista_descripcion.append(item.descripcion) 
                            lista_codigo.append(item.codigo_unico) 
            else:
                for item in self.__lista_insumos:
                    if item.activo: # Cargo solo los activos
                        lista_descripcion.append(item.descripcion) 
                        lista_codigo.append(item.codigo_unico) 
            
            self.__entry_descripcion['values']= lista_descripcion 

            # Recargo lista con nva seleccion
            self.__list_lista_insumos.delete(0, 'end') 
            index=0
            for item in lista_codigo:
                fila = str(item)+' - '+ str(lista_descripcion[index])
                self.__list_lista_insumos.insert('end',fila)
                index+=1   

    def clicklist(self,event):
        selected=event.widget.get(ANCHOR)
        lista_split = selected.split(sep='-', maxsplit=1)

        insumo_codigo_unico=lista_split[0]
        insumo_codigo_unico=insumo_codigo_unico.replace(" ", "")

        descripcion_insumo= lista_split[1]
        descripcion_insumo=descripcion_insumo.replace(" ", "")
        self.__entry_descripcion.delete(0,END)
        self.__entry_descripcion.insert(0,descripcion_insumo)
        self.__lbl_codigo_insumo['text']=insumo_codigo_unico 
#####################################################################
###############Fin Formularios  REGISTROS############################
#####################################################################

#####################################################################
###################Formularios  Insumos############################
#####################################################################

######################Formulario Baja_Insumos##################################

class FormBaja_insumo():
    """
    Clase utilizada para la generacion de 
    un formulario de baja.
    """

    def __init__(self):
        """
        Inicializacion de formulario baja
        """

        def on_closing(self):
                """
                Detecta cuando se cierra la ventana
                de formulario de baja
                """
                self.__closing=True
                self.__master.destroy()

        self.__closing=False

        self.__master =  Toplevel()

        self.__master.protocol("WM_DELETE_WINDOW", lambda :on_closing(self))
        self.__master.configure(bg="gray")

        ## Creacion de header
        self.__header_frame = Frame(self.__master, bg="gray", 
                                    bd=5, height=20, relief=FLAT)

        # Elements of header Frame
        self.__header = Label(
            self.__header_frame,
            text="Formulario de Baja",
            foreground="white",
            bg="gray",
            font=("calibri", 15),
        )
        self.__header.grid(row=0, column=0)
        self.__header_frame.pack(fill=X)


        #### Container Frame
        self.__container = Frame(self.__master, bg="cyan", 
                                bd=5, relief=SUNKEN)

        self.__lbl_codigo_unico = Label(self.__container,text='ID a eliminar:',
                             font=("calibri", 15)  )        
        self.__lbl_codigo_unico.grid(row=0, column=0)

        self.__entry_codigo_unico = Entry(self.__container, textvariable='hola',
                                font=("calibri", 15))
        
        self.__entry_codigo_unico.grid(row=0, column=1)
        self.__entry_codigo_unico.bind('<KeyRelease>', self.checkkey)

        self.__lbl_lista = Label(self.__container,text='Lista de insumos:',
                             font=("calibri", 15) )  
        self.__lbl_lista.grid(row=1, column=0,columnspan=2 )

        self.__list_lista_insumos = Listbox(self.__container)
        self.__list_lista_insumos.grid(row=2, column=0,columnspan=2 )
        self.__list_lista_insumos.bind('<<ListboxSelect>>', self.clicklist)


        self.__btn_aceptar = Button(self.__container, text="Aceptar",  
                                  font=("calibri", 15), command=lambda :aceptar(self))
        self.__btn_aceptar.grid(row=3, column=0)

        self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                    font=("calibri", 15), command= lambda :cancelar(self))
        self.__btn_cancelar.grid(row=3, column=1)

        self.__container.pack(fill=BOTH)


        ##################### Cargo lista a la lista descripcion###########################
        self.__lista_insumos=[]
        lista_descripcion=[]
        self.__lista_insumos = modulo_bd.buscar_insumo_all()
        
        for insumo in self.__lista_insumos:
            
            fila = str(insumo.codigo_unico)+ ' - '  +str(insumo.descripcion)  
            print(fila)
            lista_descripcion.append(fila )
     
        for item in lista_descripcion:
            self.__list_lista_insumos.insert('end',item)
        


        ######################  Aceptar/Cancelar  #######################################
        def aceptar(self):
            """
            Genera alta en BD
            """
            codigo_unico = self.__entry_codigo_unico.get() 
            modulo_bd.eliminar_insumo(codigo_unico)

            self.__master.destroy()
            

        def cancelar(self):
            """
            Cierra ventana de baja
            """
            globales.formBajaShowing=False
            self.__deleted=False
            self.__master.destroy()

        self.__master.grab_set()
        self.__master.focus_force()
        self.__master.wait_window()


    def isclosing(self):
        return (self.__closing)  

    def checkkey(self,event):
        value=event.widget.get() 
        lista_descripcion=[]
        if value != '': 
            for item in self.__lista_insumos: 
                if value.lower() in str(item.codigo_unico).lower():
                    fila =str( item.codigo_unico)+' - '+str(item.descripcion)
                    lista_descripcion.append(fila) 

        else: 
            for item in self.__lista_insumos: 
                fila =str( item.codigo_unico)+' - '+str(item.descripcion)
                lista_descripcion.append(fila)        
        
        self.__list_lista_insumos.delete(0, 'end') 
        for item in lista_descripcion:
            self.__list_lista_insumos.insert('end',item)
        
    def clicklist(self,event):
        selected=event.widget.get(ANCHOR)
        lista_split = selected.split(sep='-', maxsplit=1)
        codigo_unico= lista_split[0]
        codigo_unico=codigo_unico.replace(" ", "")
        self.__entry_codigo_unico.delete(0,END)
        self.__entry_codigo_unico.insert(0,codigo_unico)

 

######################Formulario Alta_Insumos##################################

class FormAlta_insumo():
    """
    Clase utilizada para la generacion de 
    un formulario de alta.
    """
    def __init__(self):
        """
        Inicializacion de formulario alta
        """
 

        def on_closing(self):
                """
                Detecta cuando se cierra la ventana
                de formulario de alta
                """
                self.__closing=True
                self.__master.destroy()

        self.__closing=False

        self.__master =  Toplevel()

        self.__master.protocol("WM_DELETE_WINDOW", lambda :on_closing(self))
        self.__master.configure(bg="gray")

        ## Creacion de header
        self.__header_frame = Frame(self.__master, bg="gray", bd=5, height=20, relief=FLAT)

        # Elements of header Frame
        self.__header = Label(
            self.__header_frame,
            text="Formulario de Alta",
            foreground="white",
            bg="gray",
            font=("calibri", 15),
        )
        self.__header.grid(row=0, column=0)
        self.__header_frame.pack(fill=X)


        #### Container Frame
        self.__container = Frame(self.__master, bg="cyan", bd=5, relief=SUNKEN)

        self.__lbl_descripcion = Label (self.__container,text='Descripcion:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_descripcion.grid(row=0, column=0)

        self.__entry_descripcion = Entry(self.__container, font=("calibri", 15))
        self.__entry_descripcion.grid(row=0, column=1)

        self.__lbl_codigo_unico = Label(self.__container,text='Codigo Unico:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_codigo_unico.grid(row=1, column=0)

        self.__entry_codigo_unico = Entry(self.__container, font=("calibri", 15))
        self.__entry_codigo_unico.grid(row=1, column=1)

        self.__lbl_activo = Label(self.__container,text='Activo:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_activo.grid(row=2, column=0)

        self.__entry_activo = ttk.Checkbutton(self.__container)
        self.__entry_activo.grid(row=2, column=1)
        self.__entry_activo.state(['!alternate']) #Debo bajar este flag primero.
        self.__entry_activo.state(['!selected']) 

        self.__btn_aceptar = Button(self.__container, text="Aceptar", 
                                    font=("calibri", 15), command=lambda :aceptar(self))
        self.__btn_aceptar.grid(row=4, column=0)

        self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                    font=("calibri", 15), command= lambda :cancelar(self))
        self.__btn_cancelar.grid(row=4, column=1)

        self.__container.pack(fill=BOTH)
       


        ######################  Aceptar/Cancelar  #######################################
        def aceptar(self):
            """
            Genera alta en la BD
            """
          
            descripcion = self.__entry_descripcion.get()
            codigo_unico = self.__entry_codigo_unico.get()
            if  'selected' in self.__entry_activo.state() : # State devuelve una tupla con varios datos sobre el check, entre ellos, el estado
                activo = True
            else:
                activo = False


            if (validacion.validacion('abc')): # Esto dara siempre verdadero, adaptar.
                if (validacion.validacion_numerica(codigo_unico)):
                    modulo_bd.alta_insumo( descripcion = descripcion, 
                                    codigo_unico = codigo_unico, 
                                    activo = activo)
                    self.__master.destroy()    
                else:
                        showinfo('Error ',  
                                'Por favor, ingrese un valor numerico en codigo unico')
            else:
                showinfo('Error',
                        'Titulo no cumple con el formato permitido de ingreso')   
            

        def cancelar(self):
            """
            Cierra ventana de  alta
            """

            self.__master.destroy()

        self.__master.grab_set()
        self.__master.focus_force()
        self.__master.wait_window()    



    def isclosing(self):
        return (self.__closing)   
        
######################Formulario Buscar_Insumos#################################

class FormBuscar_insumo():
    """
    Clase utilizada para la generacion de 
    un formulario de busqueda.
    """
    def __init__(self):
        """
        Inicializacion de formulario de busqueda
        """

        def on_closing(self):
                """
                Detecta cuando se cierra la ventana
                de formulario de busqueda
                """
                self.__closing=True
                self.__master.destroy()

        self.__closing=False

        self.__master =  Toplevel()
  
        self.__master.protocol("WM_DELETE_WINDOW", lambda :on_closing(self))
        self.__master.configure(bg="gray")

        ## Creacion de header
        self.__header_frame = Frame(self.__master, bg="gray", bd=5, 
                                    height=20, relief=FLAT)

        # Elements of header Frame
        self.__header = Label(
            self.__header_frame,
            text="Formulario de Busqueda",
            foreground="white",
            bg="gray",
            font=("calibri", 15),
        )
        self.__header.grid(row=0, column=0)
        self.__header_frame.pack(fill=X)


        #### Container Frame
        self.__container = Frame(self.__master, bg="cyan", bd=5, relief=SUNKEN)

        self.__lbl_codigo_unico_header = Label(self.__container,text='codigo unico:', 
                                    bg="cyan", font=("calibri", 15)  )
        self.__lbl_codigo_unico_header.grid(row=0, column=0)

        self.__entry_codigo_unico = Entry(self.__container,bg="cyan",font=("calibri", 15))
        self.__entry_codigo_unico.grid(row=0, column=1)
        self.__entry_codigo_unico.bind('<KeyRelease>', self.checkkey)


        self.__lbl_lista = Label (self.__container,text='Lista de Insumos :', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_lista.grid(row=0, column=2)

        self.__list_lista_insumos = Listbox (self.__container, 
                        bg="cyan", font=("calibri", 15)  )
        self.__list_lista_insumos.grid(row=1, column=2, rowspan=2)
        self.__list_lista_insumos.bind('<<ListboxSelect>>', self.clicklist)

        self.__lbl_descripcionheader = Label(self.__container,text='descripcion:', 
                                            bg="cyan", font=("calibri", 15)  )
        self.__lbl_descripcionheader.grid(row=1, column=0)

        self.__lbl_descripcion =  Label(self.__container, 
                                        bg="cyan", font=("calibri", 15))
        self.__lbl_descripcion.grid(row=1, column=1)



        self.__lbl_activo_header = Label (self.__container,text='Activo:', 
                                        bg="cyan", font=("calibri", 15)  )
        self.__lbl_activo_header.grid(row=2, column=0)

        self.__Checkbutton_activo = ttk.Checkbutton(self.__container,state=DISABLED)
        self.__Checkbutton_activo.grid(row=2, column=1)
        self.__Checkbutton_activo.state(['!alternate']) # debo bajar este estado, para poder usar el resto.

        # self.__btn_aceptar = Button(self.__container, text="Buscar",  
        #                             font=("calibri", 15), command=lambda :aceptar(self))
        # self.__btn_aceptar.grid(row=3, column=0)

        self.__btn_cancelar = Button(self.__container, text="Cerrar", 
                                    font=("calibri", 15), command= lambda :cancelar(self))
        
        self.__btn_cancelar.grid(row=3, column=0, columnspan=3)

        self.__container.pack(fill=BOTH)

        ##################### Cargo lista a la lista descripcion###########################
        self.__lista_insumos=[]
        lista_descripcion=[]
        self.__lista_insumos = modulo_bd.buscar_insumo_all()
        
        for insumo in self.__lista_insumos:
            
            fila = str(insumo.codigo_unico)+ ' - '  +str(insumo.descripcion)  
            print(fila)
            lista_descripcion.append(fila )
     
        for item in lista_descripcion:
            self.__list_lista_insumos.insert('end',item)
       


        ######################  Aceptar/Cancelar  #######################################
        def aceptar(self):
            """
            Realiza busqeda en BD
            """
            ID = self.__entry_ID.get() 
            if (validacion.validacion_numerica(ID)):
                row = modulo_bd.buscar_insumo(ID)  
                row = tuple(row)
                for x in row:
                    
                    self.__lbl_descripcion['text']= x.descripcion
                    self.__lbl_codigo_unico['text']= x.codigo_unico
                    self.__lbl_activo['text']= x.activo
            else:
                showinfo('Error en ID',
                        'Por favor, ingrese un valor numerico en ID')

        def cancelar(self):
            """
            Cierra ventana de busqueda
            """
            globales.formBajaShowing=False

            self.__master.destroy()
        
        self.__master.grab_set()
        self.__master.focus_force()
        self.__master.wait_window()    


    def isclosing(self):
        return (self.__closing)   

    def checkkey(self,event):
        value=event.widget.get() 
        
        lista_descripcion=[]
        if value != '': 
            for item in self.__lista_insumos: 
                if value.lower() in str(item.codigo_unico).lower():
                    fila =str( item.codigo_unico)+' - '+str(item.descripcion)
                    lista_descripcion.append(fila) 

        else: 
            for item in self.__lista_insumos: 
                fila =str( item.codigo_unico)+' - '+str(item.descripcion)
                lista_descripcion.append(fila)        
        
        self.__list_lista_insumos.delete(0, 'end') 
        for item in lista_descripcion:
            self.__list_lista_insumos.insert('end',item)


    def clicklist(self,event):
        selected=event.widget.get(ANCHOR)
        lista_split = selected.split(sep='-', maxsplit=1)
        codigo_unico= lista_split[0]
        codigo_unico=codigo_unico.replace(" ", "")
        self.__entry_codigo_unico.delete(0,END)
        self.__entry_codigo_unico.insert(0,codigo_unico)

        insumo = modulo_bd.buscar_insumo_by_codigo(codigo_unico)
        
        self.__lbl_descripcion['text']= insumo[0].descripcion
        if insumo[0].activo== True:
            self.__Checkbutton_activo.state(['selected'])
        else :
            self.__Checkbutton_activo.state(['!selected'])
        
######################Formulario Modificar_Insumos##############################

class FormModificar_insumo():


    """
    Clase utilizada para la generacion de 
    un formulario de modificacion.
    
    """
    def __init__(self,*args):
        """
        Inicializacion de formulario de modificacion
        """
        
       

        def on_closing(self):
                """
                Detecta cuando se cierra la ventana
                de formulario de modificacion
                """
                self.__closing=True
                self.__master.destroy()

        self.__closing=False

        self.__master =  Toplevel()
        self.__master.protocol("WM_DELETE_WINDOW", lambda :on_closing(self))
        self.__master.configure(bg="gray")

        ## Creacion de header
        self.__header_frame = Frame(self.__master, bg="gray", 
                                    bd=5, height=20, relief=FLAT)

        # Elements of header Frame
        self.__header = Label(
            self.__header_frame,
            text="Formulario de Modificacion",
            foreground="white",
            bg="gray",
            font=("calibri", 15),
        )
        self.__header.grid(row=0, column=0)
        self.__header_frame.pack(fill=X)


        #### Container Frame
        self.__container = Frame(self.__master, bg="cyan", bd=5, relief=SUNKEN)
        
        self.__lbl_ID = Label (self.__container,text='ID:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_ID.grid(row=0, column=0)

        self.__entry_ID = Entry(self.__container, font=("calibri", 15))
        self.__entry_ID.grid(row=0, column=1)
        self.__entry_ID.insert(0,str(args[0][0]))

        self.__lbl_descripcion = Label (self.__container,text='descripcion:', 
                                        bg="cyan", font=("calibri", 15)  )
        self.__lbl_descripcion.grid(row=0, column=0)

        self.__entry_descripcion = Entry(self.__container,
                                        font=("calibri", 15))
        
        self.__entry_descripcion.grid(row=0, column=1)
        self.__entry_descripcion.insert(0,str(args[0][1]))
        


        self.__lbl_codigo_unico = Label (self.__container,text='Codigo Unico:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_codigo_unico.grid(row=1, column=0)

        self.__entry_codigo_unico = Entry(self.__container, font=("calibri", 15))
        self.__entry_codigo_unico.grid(row=1, column=1)
        self.__entry_codigo_unico.insert(0,str(args[0][2]))

        self.__lbl_activo = Label (self.__container,text='Activo:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_activo.grid(row=2, column=0)

        self.__entry_activo = ttk.Checkbutton(self.__container)
        self.__entry_activo.grid(row=2, column=1)
        self.__entry_activo.state(['!alternate']) # debo bajar este estado, para poder usar el resto.
        
        if (str(args[0][3])== 'True'):
            self.__entry_activo.state(['selected']) 
            # print('Considero verdadero, es:')
            print(str(args[0][3]))
        else:
            self.__entry_activo.state(['!disabled']) 
            # print('Considero falso, es:')
            print(str(args[0][3]))
          

        self.__btn_aceptar = Button(self.__container, text="Aceptar",  
                                    font=("calibri", 15), command=lambda :aceptar(self))
        self.__btn_aceptar.grid(row=3, column=0)

        self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                    font=("calibri", 15), command= lambda :cancelar(self))
        self.__btn_cancelar.grid(row=3, column=1)

        self.__container.pack(fill=BOTH)
       


        ######################  Aceptar/Cancelar  #######################################
        def aceptar(self):
            """
            Genera modificacion en BD
            """
            id= self.__entry_ID.get()
            descripcion = self.__entry_descripcion.get()
            codigo_unico = self.__entry_codigo_unico.get()
            
            if  'selected' in self.__entry_activo.state() :
                activo = True
            else:
                activo = False



            print(id + ' '+ descripcion+ ' ' + codigo_unico+ ' '+ str(activo) )

            if (validacion.validacion('abc')): #Validacion no usada en este caso
                if (validacion.validacion_numerica(codigo_unico)):
                    modulo_bd.modificar_insumo(id=id,
                                        descripcion=descripcion,
                                        codigo_unico=codigo_unico,
                                        activo=activo)
                    self.__master.destroy()
                    
                else:
                    showinfo('Error de formato','Por favor, ingrese un valor'
                            ' numerico en cantidad')
            else:
                showinfo('Error de Formato','titulo no cumple con el' 
                        'formato permitido de ingreso')
         

        def cancelar(self):
            """
            Cierra ventana de modificacion
            """
            globales.formBajaShowing=False
  
            self.__master.destroy()

        self.__master.grab_set()
        self.__master.focus_force()
        self.__master.wait_window()  


    def isclosing(self):
        return (self.__closing)   


#####################################################################
###############Fin Formularios  Insumos##############################
#####################################################################


#####################################################################
###################Formularios Autenticacion#########################
#####################################################################
class Form_registrar_usuario():
    
    def __init__(self,admin=False):  
    
            self.__master =  Toplevel()
            self.__master.configure(bg="gray")
            self.__admin= admin

            ## Creacion de header
            self.__header_frame = Frame(self.__master, bg="gray", 
                                        bd=5, height=20, relief=FLAT)

            # Elements of header Frame
            self.__header = Label(
                self.__header_frame,
                text="Formulario de Alta de Registros",
                foreground="white",
                bg="gray",
                font=("calibri", 15),
            )
            self.__header.grid(row=0, column=0)
            self.__header_frame.pack(fill=X)


            #### Container Frame
            self.__container = Frame(self.__master, bg="cyan", bd=5, relief=SUNKEN)
            
            self.__lbl_usuario_header = Label (self.__container,text='Usuario:', 
                                    bg="cyan", font=("calibri", 15)  )
            self.__lbl_usuario_header.grid(row=0, column=0)


            self.__entry_usuario = Entry(self.__container, font=("calibri", 15))
            self.__entry_usuario.grid(row=0, column=1)

            self.__lbl_password_header = Label (self.__container,text='Contraseña:', 
                                    bg="cyan", font=("calibri", 15)  )
            self.__lbl_password_header.grid(row=1, column=0)


            self.__entry_password = Entry(self.__container, font=("calibri", 15), show="*")
            self.__entry_password.grid(row=1, column=1)

            self.__lbl_password_confirmar_header = Label (self.__container,text=' Confirmar Contraseña:', 
                                    bg="cyan", font=("calibri", 15)  )
            self.__lbl_password_confirmar_header.grid(row=2, column=0)


            self.__entry_password_confirmar = Entry(self.__container, font=("calibri", 15), show="*")
            self.__entry_password_confirmar.grid(row=2, column=1)

            if self.__admin:
                self.__lbl_perfil = Label(self.__container,text='Administrador:', 
                                        bg="cyan", font=("calibri", 15)  )
                self.__lbl_perfil.grid(row=3, column=0)

                self.__entry_perfil = ttk.Checkbutton(self.__container)
                self.__entry_perfil.grid(row=3, column=1)
                self.__entry_perfil.state(['!alternate']) #Debo bajar este flag primero.
                self.__entry_perfil.state(['!selected']) 

            
            self.__btn_aceptar = Button(self.__container, text="Aceptar",  
                                        font=("calibri", 15), command=lambda :aceptar(self))
            self.__btn_aceptar.grid(row=4, column=0)

            self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                        font=("calibri", 15), command= lambda :cancelar(self))
            self.__btn_cancelar.grid(row=4, column=1)

            self.__container.pack(fill=BOTH)


            def aceptar(self):
                """
                Genera modificacion en BD
                """
                usuario_name= self.__entry_usuario.get()
                password= bytes(self.__entry_password.get(),'utf-8')
                password_confirmar = bytes(self.__entry_password_confirmar.get(),'utf-8')
                administrador = False

                if self.__admin :
                            
                    if  'selected' in self.__entry_perfil.state() : # State devuelve una tupla con varios datos sobre el check, entre ellos, el estado
                        administrador = True
                    else:
                        administrador = False

        

                if (validacion.validacion('abc')): #Validacion no usada en este caso (validar usuario)
                    if (validacion.validacion_numerica('123')): #Validacion no usada en este caso (validar password)
                        if password == password_confirmar:          # Si las contraseñas son iguales
                            salt= b'aleaotorio'
                            h = hashlib.pbkdf2_hmac('sha256',password, salt, 100)
                            password_encriptado = h.hex()
                            #doy de alta
                            print(usuario_name + ' '+ str(password)+ ' ' +str(password_confirmar)+ ' '+ str(administrador) + ' '+ str(password_encriptado) )
                            modulo_bd.alta_usuario(usuario_name= usuario_name, password= password_encriptado, admin=administrador)
                            showinfo('-','Usuario creado correctamente')
                        else:
                            showinfo('-','Por favor, confirme la contraseña correctamente')

            
                        self.__master.destroy()
                        
                    else:
                        showinfo('Error de formato','Por favor, ingrese un valor'
                                ' numerico en cantidad')
                else:
                    showinfo('Error de Formato','titulo no cumple con el' 
                            'formato permitido de ingreso')
                

            def cancelar(self):
                """
                Cierra ventana de modificacion
                """
                globales.formBajaShowing=False

                self.__master.destroy()

            self.__master.grab_set()
            self.__master.focus_force()
            self.__master.wait_window()  



class Form_baja_usuario():

    """
    Clase utilizada para la generacion de 
    un formulario de baja.
    """

    def __init__(self):
        
            """
            Inicializacion de formulario baja
            """

            self.__master =  Toplevel()
            self.__master.configure(bg="gray")

            ## Creacion de header
            self.__header_frame = Frame(self.__master, bg="gray", 
                                        bd=5, height=20, relief=FLAT)

            # Elements of header Frame
            self.__header = Label(
                self.__header_frame,
                text="Formulario de Baja",
                foreground="white",
                bg="gray",
                font=("calibri", 15),
            )
            self.__header.grid(row=0, column=0)
            self.__header_frame.pack(fill=X)


            #### Container Frame
            self.__container = Frame(self.__master, bg="cyan", 
                                    bd=5, relief=SUNKEN)

            self.__lbl_user_name = Label(self.__container,text='ID a eliminar:',
                                font=("calibri", 15) ,bg="cyan" )        
            self.__lbl_user_name.grid(row=0, column=0)

            self.__entry_user_name = Entry(self.__container, textvariable='hola',
                                    font=("calibri", 15))
            
            self.__entry_user_name.grid(row=0, column=1)
            self.__entry_user_name.bind('<KeyRelease>', self.checkkey)

            self.__lbl_lista = Label(self.__container,text='Lista de usuarios:',
                                font=("calibri", 15),bg="cyan" )  
            self.__lbl_lista.grid(row=1, column=0,columnspan=2 )

            self.__list_lista_usuarios = Listbox(self.__container)
            self.__list_lista_usuarios.grid(row=2, column=0,columnspan=2 )
            self.__list_lista_usuarios.bind('<<ListboxSelect>>', self.clicklist)


            self.__btn_aceptar = Button(self.__container, text="Aceptar",  
                                    font=("calibri", 15), command=lambda :aceptar(self))
            self.__btn_aceptar.grid(row=3, column=0)

            self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                        font=("calibri", 15), command= lambda :cancelar(self))
            self.__btn_cancelar.grid(row=3, column=1)

            self.__container.pack(fill=BOTH)


            ##################### Cargo lista a la lista descripcion###########################
            self.__lista_usuarios=[]
            lista_user_name=[]
            self.__lista_usuarios = modulo_bd.buscar_usuarios_all()
            
            for usuario in self.__lista_usuarios:
                
                fila = str(usuario.usuario)+ ' - '  +str(usuario.admin)  
                print(fila)
                lista_user_name.append(fila )
        
            for item in lista_user_name:
                self.__list_lista_usuarios.insert('end',item)
            


            ######################  Aceptar/Cancelar  #######################################
            def aceptar(self):
                """
                Genera alta en BD
                """
                usuario_name = self.__entry_user_name.get() 
                modulo_bd.eliminar_usuario(usuario_name)

                self.__master.destroy()
                

            def cancelar(self):
                """
                Cierra ventana de baja
                """
                self.__master.destroy()

            self.__master.grab_set()
            self.__master.focus_force()
            self.__master.wait_window()



    def checkkey(self,event):
        value=event.widget.get() 
        lista_usuarios=[]
        if value != '': 
            for item in self.__lista_usuarios: 
                if value.lower() in str(item.usuario).lower():
                    fila =str( item.usuario)+' - '+str(item.admin)
                    lista_usuarios.append(fila) 

        else: 
            for item in self.__lista_usuarios: 
                fila =str( item.usuario)+' - '+str(item.admin)
                lista_usuarios.append(fila)        
        
        self.__list_lista_usuarios.delete(0, 'end') 
        for item in lista_usuarios:
            self.__list_lista_usuarios.insert('end',item)
        
    def clicklist(self,event):
        selected=event.widget.get(ANCHOR)
        lista_split = selected.split(sep='-', maxsplit=1)
        usuario_name= lista_split[0]
        usuario_name=usuario_name.replace(" ", "")
        self.__entry_user_name.delete(0,END)
        self.__entry_user_name.insert(0,usuario_name)

#####################################################################
###############Fin Formularios  Autenticacion########################
#####################################################################

class Form_reiniciar_password():
        def __init__(self):
        
            """
            Inicializacion de formulario baja
            """

            self.__master =  Toplevel()
            self.__master.configure(bg="gray")

            ## Creacion de header
            self.__header_frame = Frame(self.__master, bg="gray", 
                                        bd=5, height=20, relief=FLAT)

            # Elements of header Frame
            self.__header = Label(
                self.__header_frame,
                text="Formulario de Baja",
                foreground="white",
                bg="gray",
                font=("calibri", 15),
            )
            self.__header.grid(row=0, column=0)
            self.__header_frame.pack(fill=X)


            #### Container Frame
            self.__container = Frame(self.__master, bg="cyan", 
                                    bd=5, relief=SUNKEN)

            self.__lbl_user_name = Label(self.__container,text='Ingrese usuario:',
                                font=("calibri", 15)  )        
            self.__lbl_user_name.grid(row=0, column=0)

            self.__entry_user_name = Entry(self.__container, textvariable='hola',
                                    font=("calibri", 15))
            
            self.__entry_user_name.grid(row=0, column=1)

            # self.__lbl_nuevo_password= Label(self.__container,text='Nueva contraseña',
            #                     font=("calibri", 15)  )        
            # self.__lbl_nuevo_password.grid(row=1, column=0)


            self.__btn_aceptar = Button(self.__container, text="Aceptar", 
                                        font=("calibri", 15), command=lambda :aceptar(self))
            self.__btn_aceptar.grid(row=2, column=0)

            self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                        font=("calibri", 15), command= lambda :cancelar(self))
            self.__btn_cancelar.grid(row=2, column=1)

            self.__container.pack(fill=BOTH)


            def aceptar(self):
                    usuario_name= self.__entry_user_name.get()
                    password= get_random_alphanumeric_string(5,3)
                    password= bytes(password,'utf-8')

                    if (validacion.validacion('abc')): #Validacion no usada en este caso (validar usuario)
                        if (validacion.validacion_numerica('123')): #Validacion no usada en este caso (validar password)
                          
                                salt= b'aleaotorio'
                                h = hashlib.pbkdf2_hmac('sha256',password, salt, 100)
                                password_encriptado = h.hex()
                                #doy de alta
                                print(usuario_name + ' '+ str(password)+ ' ' + str(password_encriptado) )
                                modulo_bd.actualizar_usuario(usuario_name= usuario_name, password= password_encriptado)
                                msje= 'Su nueva contraseña es: '+ password.decode('utf-8')
                                showinfo('-',msje)


                
                                self.__master.destroy()
                            
                        else:
                            showinfo('Error de formato','Por favor, ingrese un valor'
                                    ' numerico en cantidad')
                    else:
                        showinfo('Error de Formato','titulo no cumple con el' 
                                'formato permitido de ingreso')



            def cancelar(self):
                """
                Cierra ventana de modificacion
                """
                globales.formBajaShowing=False

                self.__master.destroy()

            self.__master.grab_set()
            self.__master.focus_force()
            self.__master.wait_window()  


def get_random_alphanumeric_string(letters_count, digits_count):
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    sample_str += ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert string to list and shuffle it to mix letters and digits
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string


class Form_cambiar_password():
        def __init__(self):
        
            """
            Inicializacion de formulario baja
            """

            self.__master =  Toplevel()
            self.__master.configure(bg="gray")

            ## Creacion de header
            self.__header_frame = Frame(self.__master, bg="gray", 
                                        bd=5, height=20, relief=FLAT)

            # Elements of header Frame
            self.__header = Label(
                self.__header_frame,
                text="Cambio de contraseña",
                foreground="white",
                bg="gray",
                font=("calibri", 15),
            )
            self.__header.grid(row=0, column=0)
            self.__header_frame.pack(fill=X)


            #### Container Frame
            self.__container = Frame(self.__master, bg="cyan", 
                                    bd=5, relief=SUNKEN)

            self.__lbl_user_name = Label(self.__container,text='Ingrese usuario:',
                                font=("calibri", 15) , bg="cyan" )        
            self.__lbl_user_name.grid(row=0, column=0)

            self.__entry_user_name = Entry(self.__container,
                                    font=("calibri", 15))
            
            self.__entry_user_name.grid(row=0, column=1)

            self.__lbl_nuevo_password_anterior= Label(self.__container,text='Ingrese contraseña anterior:',
                                         font=("calibri", 15), bg="cyan"  )        
            self.__lbl_nuevo_password_anterior.grid(row=1, column=0)

            self.__entry_password_anterior = Entry(self.__container,
                                             font=("calibri", 15), show="*")
            
            self.__entry_password_anterior.grid(row=1, column=1)

            self.__lbl_nuevo_password_nuevo= Label(self.__container,text='Ingrese nueva contraseña:',
                                         font=("calibri", 15) , bg="cyan" )        
            self.__lbl_nuevo_password_nuevo.grid(row=2, column=0)

            self.__entry_password_nuevo = Entry(self.__container,
                                             font=("calibri", 15), show="*")
            
            self.__entry_password_nuevo.grid(row=2, column=1)


            self.__btn_aceptar = Button(self.__container, text="Aceptar", 
                                        font=("calibri", 15), command=lambda :aceptar(self))
            self.__btn_aceptar.grid(row=3, column=0)

            self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                        font=("calibri", 15), command= lambda :cancelar(self))
            self.__btn_cancelar.grid(row=3, column=1)

            self.__container.pack(fill=BOTH)


            def aceptar(self):
                    usuario_name= self.__entry_user_name.get()
                    password_anterior= self.__entry_password_anterior.get()
                    password_nuevo=self.__entry_password_nuevo.get()


                    password_anterior= bytes(password_anterior,'utf-8')
                    password_nuevo=bytes(password_nuevo,'utf-8')

                    if (validacion.validacion('abc')): #Validacion no usada en este caso (validar usuario)
                        if (validacion.validacion_numerica('123')): #Validacion no usada en este caso (validar password)
                          
                                salt= b'aleaotorio'
                                # ·encripto contraseña anterior y nueva
                                h = hashlib.pbkdf2_hmac('sha256',password_anterior, salt, 100)
                                password_anterior_encriptado = h.hex()

                                h = hashlib.pbkdf2_hmac('sha256',password_nuevo, salt, 100)
                                password_nuevo_encriptado = h.hex()                            

                                usuario_actualizar= modulo_bd.buscar_usuario(usuario_name=usuario_name, password= password_anterior_encriptado)                               
                               
                                if len(usuario_actualizar)>0:
                                    #actualizo
                                    # print(usuario_name + ' '+ str(password)+ ' ' + str(password_encriptado) )

                                    modulo_bd.actualizar_usuario(usuario_name= usuario_name, password= password_nuevo_encriptado, admin=usuario_actualizar[0].admin)
                                    msje= 'Cambio de contraseña realizado con exito'
                                    showinfo('-',msje)
                                    self.__master.destroy()
                                else:
                                    showinfo('-', 'Usuario o contraseña anterior no correspondiente')


                

                            
                        else:
                            showinfo('Error de formato','Por favor, ingrese un valor'
                                    ' numerico en cantidad')
                    else:
                        showinfo('Error de Formato','titulo no cumple con el' 
                                'formato permitido de ingreso')



            def cancelar(self):
                """
                Cierra ventana de modificacion
                """
                globales.formBajaShowing=False

                self.__master.destroy()

            self.__master.grab_set()
            self.__master.focus_force()
            self.__master.wait_window()  



class Form_editar_perfil_usuario():
    def __init__(self,*args):
        """
        Inicializacion de formulario de modificacion
        """
        self.__usuario =str(args[0][1])
        self.__password =bytes(args[0][2],'utf-8')
        self.__admin =str(args[0][3])

        print(self.__usuario +' ' + self.__password.decode('utf-8') +' ' + str(self.__admin))
 
        self.__master =  Toplevel()
        self.__master.configure(bg="gray")

        ## Creacion de header
        self.__header_frame = Frame(self.__master, bg="gray", 
                                    bd=5, height=20, relief=FLAT)

        # Elements of header Frame
        self.__header = Label(
            self.__header_frame,
            text="Formulario de Modificacion",
            foreground="white",
            bg="gray",
            font=("calibri", 15),
        )
        self.__header.grid(row=0, column=0)
        self.__header_frame.pack(fill=X)


        #### Container Frame
        self.__container = Frame(self.__master, bg="cyan", bd=5, relief=SUNKEN)
        
        self.__lbl_usuario_header = Label (self.__container,text='Usuario:', 
                                bg="cyan", font=("calibri", 15)  )
        self.__lbl_usuario_header .grid(row=0, column=0)

        self.__lbl_usuario = Label(self.__container, font=("calibri", 15), bg='cyan')
        self.__lbl_usuario.grid(row=0, column=1)
        self.__lbl_usuario['text']=str(self.__usuario)

        self.__lbl_perfil = Label (self.__container,text='Administrador:', 
                                        bg="cyan", font=("calibri", 15)  )
        self.__lbl_perfil.grid(row=1, column=0)


        self.__entry_perfil = ttk.Checkbutton(self.__container)
        self.__entry_perfil.grid(row=1, column=1)
        self.__entry_perfil.state(['!alternate']) #Debo bajar este flag primero.
        if (self.__admin== 'True'): # " Leo el campo admin de ese usuario y seteo"
            self.__entry_perfil.state(['selected']) 
        else:
            self.__entry_perfil.state(['!selected']) 
        

          

        self.__btn_aceptar = Button(self.__container, text="Aceptar",  
                                    font=("calibri", 15), command=lambda :aceptar(self))
        self.__btn_aceptar.grid(row=2, column=0)

        self.__btn_cancelar = Button(self.__container, text="Cancelar", 
                                    font=("calibri", 15), command= lambda :cancelar(self))
        self.__btn_cancelar.grid(row=2, column=1)

        self.__container.pack(fill=BOTH)
       


        ######################  Aceptar/Cancelar  #######################################
        def aceptar(self):
            """
            Genera modificacion en BD
            """

            if self.__admin :
                        
                if  'selected' in self.__entry_perfil.state() : # State devuelve una tupla con varios datos sobre el check, entre ellos, el estado
                    self.__admin = True
                else:
                    self.__admin = False



            if (validacion.validacion('abc')): #Validacion no usada en este caso
                if (validacion.validacion_numerica('123')):
                    modulo_bd.actualizar_usuario(usuario_name= self.__usuario, password=self.__password , admin= self.__admin)
                    self.__master.destroy()
                    
                else:
                    showinfo('Error de formato','Por favor, ingrese un valor'
                            ' numerico en cantidad')
            else:
                showinfo('Error de Formato','titulo no cumple con el' 
                        'formato permitido de ingreso')
         

        def cancelar(self):
            """
            Cierra ventana de modificacion
            """
            globales.formBajaShowing=False
  
            self.__master.destroy()

        self.__master.grab_set()
        self.__master.focus_force()
        self.__master.wait_window()  

