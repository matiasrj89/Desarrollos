"""
Ejercicio integrador: 
1) Según los temas dados en el nivel inicial. 
   Crear un abmc (crud) de datos, que permita cargar como mínimo dos campos (titulo y
  descripción)
   Guardar los registros en una base de datos del tipo SQLite3.
   Validar el código del campo título para admitir sólo alfanuméricos. Se puede usar la
  siguiente regex o utilizar una propia: patron="^[A-Za-z]+(?:[ _-][A-Za-z]+)*$".
   El código debe cumplir con PEP8
2) Temas adicionados durante la cursada del nivel intermedio.
   La funcionalidad de interacción con la base de datos y validación de campos debe ubicarse en
módulos aparte.
   La app debe realizarse según el paradigma de POO (Dado a partir de la unidad 3)
   Se puede implementar el patrón MVC (Introducido en la unidad 5) (OPCIONAL)
   Se debe agregar el trabajo con excepciones (Introducido en la unidad 7)
   Se debe documentar mediante pydoc la app (Introducido en la unidad 8) 


"""

from tkinter import *
from tkinter import ttk
import modulo_grilla as mdgrilla
import sqlite3
import random
import mysql.connector
from tkinter.messagebox import *
import re
import formularios
import globales
import crud
import modulo_bd
import gestion_insumos
import auth



flag_bdcreada = FALSE
lista = []
patron = re.compile('^[A-Za-z]+(?:[ _-][A-Za-z]+)*$')

class Pagina_inicio():

  def __init__(self, parent):

      self.my_parent= parent
            
      ## Creacion de header
      header_frame = Frame(self.my_parent, bg="gray",bd=5,height=20, relief=FLAT)

      # Elements of header Frame
      header = Label(
          header_frame,
          text="BienvenidosAremote",
          foreground="white",
          bg="gray",
          font=("calibri", 15),
      )
      header.grid(row=0, column=0)
      header_frame.pack(fill=X)
      
      #### Container Frame      
      container = Frame(self.my_parent, bg="blue", bd=5, relief=SUNKEN)
      container.columnconfigure(0, weight=1)
      container.rowconfigure(0, weight=1)
      #Grilla
      frame_grilla = Frame(container) 
      grilla = ttk.Treeview(frame_grilla)
      mdgrilla.conectar(grilla, 'registros')
      grilla.grid(row=0,column=0,sticky=NSEW)
      frame_grilla.grid(row=0,column=0,sticky=NSEW)
      
      #### Btns Frame

      frame_btns = Frame(container)

      btn_alta = Button(frame_btns, text="Alta", 
                      command=lambda:crud.alta_registro(grilla))
      btn_alta.grid(row=1, column=0)


      btnModificar = Button(frame_btns, text="Modificar", 
                            command=lambda :crud.modificar_registro(grilla))
      btnModificar.grid(row=1, column=1)

      btn_baja = Button(frame_btns, text="Baja", 
                      command= lambda: crud.baja_registro(grilla))
      btn_baja.grid(row=1, column=2)

      btn_buscar = Button(frame_btns, text="Buscar", 
                        command=lambda:crud.buscar_registro(grilla))
      btn_buscar.grid(row=1, column=3)

      btn_actualizar = Button(frame_btns, text="Actualizar", 
                            command= lambda: mdgrilla.actualizar_registros(grilla))
      btn_actualizar.grid(row=1, column=4)

      btn_test = Button(frame_btns, text="test", 
                            command= lambda: self.test())
      btn_test.grid(row=1, column=5)

      frame_btns.grid(row=1,column=0,sticky=NSEW)

      mdgrilla.actualizar_registros(grilla) 

      container.pack(fill=BOTH)

  def test(self):
    try:
      # app = auth.Auth()
      auxiliar =Registros().select().where(Registros.registro_id==2)
      for x in auxiliar:

          print('DEBUG\n\n\n\n\n\n\n')
          print(str(x.lote_partida))
          print(str(x.vencimiento))
          print('insumo')
          print(str(x.insumo_id) ) ###### AQUI NO CAPTURA
      
          print(' \n\n\n\n\n\n\nFin DEBUG\n\n\n\n\n\n\n')
    except:
      print('error')




class Gestion_usuarios():

  def __init__(self, parent):

      self.my_parent= parent
            
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
      mdgrilla.conectar(grilla, 'usuarios')
      grilla.grid(row=0,column=0,sticky=W)
      frame_grilla.grid(row=0,column=0)
      


      frame_btns = Frame(container)

      btn_alta = Button(frame_btns, text="Alta", 
                      command=lambda:crud.alta_usuario(grilla))
      btn_alta.grid(row=0, column=0)

      btn_baja_usuario = Button(frame_btns, text="Baja", 
                      command=lambda:crud.baja_usuario(grilla))
      btn_baja_usuario.grid(row=0, column=1)

      btn_editar_perfil = Button(frame_btns, text="Editar Perfil", 
                      command=lambda:crud.editar_perfil_usuario(grilla))
      btn_editar_perfil.grid(row=0, column=2)

      frame_btns.grid(row=1,column=0)
      mdgrilla.actualizar_usuarios(grilla) 
      container.pack(fill=BOTH)



###################### Creacion Entorno Grafico #######################
class MyApp(Tk):
      
  def __init__(self, *configs: '[0] Boolean Admin/general'):
      Tk.__init__(self)       
      self.configure(bg="gray")
      self.geometry("400x600")
      # self.__is_admin= configs[0]
      self.__sesion_iniciada= False
    

      # Creacion de Base de datos.
     
      # try:
      #   # modulo_bd.creardb(globales.db_name)
      # except:
      #   print('Error al intentar inicializar  BD')
      

      #### Container Frame
      container = Frame(self, bg="cyan", bd=5, relief=SUNKEN)

      # Creacion de Menu

      self.__menu_bar = Menu(self,tearoff=0)

      self.__menu_archivo = Menu(self.__menu_bar,tearoff=0)
      self.__menu_archivo.add_command(label='Guardar', 
                              command= lambda: self.imprimir('guardar')) 
      self.__menu_archivo.add_command(label='Salir', command=self.destroy) 


      # menu_crud = Menu(menu_bar,tearoff=0)
      # menu_crud.add_command(label='Alta', command=lambda:self.imprimir('alta'))  
      # menu_crud.add_command(label='Modificar', 
      #                     command=lambda :self.imprimir('modificar')) 
      # menu_crud.add_command(label='Baja', command=lambda: self.imprimir('baja'))  
      # menu_crud.add_command(label='Buscar', command=lambda:self.imprimir('buscar'))  

      self.__menu_usuario = Menu(self.__menu_bar,tearoff=0)
      
      self.__menu_usuario.add_command(label='iniciar sesion', 
                                command= lambda: self.iniciar_sesion())         
      
      self.__menu_bar.add_cascade(label='Archivo',menu=self.__menu_archivo)
      # menu_bar.add_cascade(label='Gestion BD',menu=menu_crud)
      self.__menu_bar.add_cascade(label='Cuenta',menu=self.__menu_usuario)

      self.config(menu=self.__menu_bar)

      # ## Creacion de header
      # header_frame = Frame(self.my_parent, bg="gray",bd=5,height=20, relief=FLAT)

      # # Elements of header Frame
      # header = Label(
      #     header_frame,
      #     text="Bienvenidos",
      #     foreground="white",
      #     bg="gray",
      #     font=("calibri", 15),
      # )
      # header.grid(row=0, column=0)
      # header_frame.pack(fill=X)


      print("""  A continuacion, se muestra un poco de documentacion (No es necesario, solo a
      modo de muestra""")
      print(mdgrilla.actualizar_registros.__doc__)
      print(mdgrilla.actualizar_insumos.__doc__)
      print(mdgrilla.conectar.__doc__)
      print(mdgrilla.item_selected.__doc__)
      print(crud.actualizar_registro.__doc__)
      print(crud.alta_registro.__doc__)
      print(crud.modificar_registro.__doc__)
      print(crud.baja_registro.__doc__)
      print(crud.buscar_registro.__doc__)
      print(formularios.FormAlta_registro.__doc__)
      print(formularios.FormBaja_registro.__doc__)
      print(formularios.FormBaja_registro.__doc__)
      print(formularios.FormBuscar_registro.__doc__)
      # print(modulo_bd.AdminDB.__doc__)


      container.pack(fill=X)

  def refresh(self):
        if self.__sesion_iniciada:
          self.__tab_parent= ttk.Notebook(self)
          self.__tab1 = ttk.Frame(self.__tab_parent)
          self.__tab2 = ttk.Frame(self.__tab_parent)
          self.__tab3 = ttk.Frame(self.__tab_parent)
          Pagina_inicio(self.__tab1)
          gestion_insumos.inicio(self.__tab2)
          Gestion_usuarios(self.__tab3)
          self.__tab_parent.add(self.__tab1,text="Registros")
          self.__tab_parent.add(self.__tab2,text="Insumos")

          self.__menu_usuario.delete('iniciar sesion')
          self.__menu_usuario.add_command(label='cambiar contraseña', 
                                command= lambda: self.cambiar_password())

          self.__menu_usuario.add_command(label='cerrar sesion', 
                                command= lambda: self.cerrar_sesion()) 
          
          if self.__is_admin:
            self.__tab_parent.add(self.__tab3,text="Gestion de usuarios")

          self.__tab_parent.pack(fill=BOTH)



        else:
          self.__tab_parent.destroy()

          

          self.__menu_usuario.delete('cambiar contraseña')
          self.__menu_usuario.delete('cerrar sesion')
          self.__menu_usuario.add_command(label='iniciar sesion', 
                                command= lambda: self.iniciar_sesion())


  
  def imprimir(self,msj):
    showinfo ('-', msj)

  def cambiar_password(self):
    formularios.Form_cambiar_password()

  def cerrar_sesion(self):
    self.__sesion_iniciada= False
    self.refresh

  def iniciar_sesion(self):
    autenticar = auth.Auth()
    usuario_iniciado = autenticar.get_usuario()
    self.__is_admin =usuario_iniciado.admin
    self.__sesion_iniciada= True
    self.refresh()

    




app = MyApp()
app.mainloop()

