from tkinter import *
from tkinter import ttk
import modulo_grilla as mdgrilla
import sqlite3
import crud

class Gestion_insumo():
      
    def __init__(self, parent=None, **configs):
     
      self.my_parent=parent     
    

      # Creacion de Base de datos.
     
      # try:
      #   # modulo_bd.creardb(globales.db_name)
      # except:
      #   print('Error al intentar inicializar  BD')

      ## Creacion de header
      header_frame = Frame(self.my_parent, bg="gray",bd=5,height=20, relief=FLAT)

      # Elements of header Frame
      header = Label(
          header_frame,
          text="Bienvenidos",
          foreground="white",
          bg="gray",
          font=("calibri", 15),
      )
      header.grid(row=0, column=0)
      header_frame.pack(fill=X)
      

      #### Container Frame
      container = Frame(self.my_parent, bg="cyan", bd=5, relief=SUNKEN)
      
      #Grilla
      frame_grilla = Frame(container) 
      grilla = ttk.Treeview(frame_grilla)
      mdgrilla.conectar(grilla, 'insumos')
      grilla.grid(row=0,column=0,sticky=W)
      frame_grilla.grid(row=0,column=0)
      
      #### Btns Frame

      frame_btns = Frame(container)

      btn_alta = Button(frame_btns, text="Alta", 
                      command=lambda:crud.alta_insumo(grilla))
      btn_alta.grid(row=1, column=0)


      btnModificar = Button(frame_btns, text="Modificar", 
                            command=lambda :crud.modificar_insumo(grilla))
      btnModificar.grid(row=1, column=1)

    #   btn_baja = Button(frame_btns, text="Baja", 
    #                   command= lambda: crud.baja_insumo(grilla))
    #   btn_baja.grid(row=1, column=2) NO DEBO DAR DE BAJA INSUMOS; GENERO INCONSISTENCIA EN LA BD.
                                    #SOLO PUEDO DESACTIVAR INSUMOS.
      btn_buscar = Button(frame_btns, text="Buscar", 
                        command=lambda:crud.buscar_insumo(grilla))
      btn_buscar.grid(row=1, column=2)

      btn_actualizar = Button(frame_btns, text="Actualizar", 
                            command= lambda: mdgrilla.actualizar_insumos(grilla))
      btn_actualizar.grid(row=1, column=3)


      frame_btns.grid(row=2,column=0)

      ## Creacion de Menu



      mdgrilla.actualizar_insumos(grilla)
      container.pack(fill=X)


    # def destroy():
    #     self.my_parent.destroy()

def inicio(parent):
    gestion_window = Gestion_insumo(parent)
    
    
    