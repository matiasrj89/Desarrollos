from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
# import home as home
import hashlib
import modulo_bd
import formularios
import crud

class Auth(): #Antes (Tk)
    def __init__(self,parent=None):
        # Tk.__init__(self)
        self.__master=Toplevel()
        self.__usuarios= modulo_bd.Usuarios()
        # self.__master.configure(bg="gray")

        
        ## Creacion de header
        header_frame = Frame(self.__master, bg="gray",bd=5,height=20, relief=FLAT)

        # Elements of header Frame
        header = Label(
            header_frame,
            text="Autenticacion",
            foreground="white",
            bg="gray",
            font=("calibri", 15),
        )
        header.grid(row=0, column=0)
        header_frame.pack(fill=X)

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

        #### Btns Frame

        self.__frame_btns = Frame(self.__container)

        btn_iniciar_sesion = Button(self.__frame_btns, text="Iniciar Sesion", 
                        command= lambda: self.iniciar_sesion())
        btn_iniciar_sesion.grid(row=2, column=0, columnspan=1)


        btn_registrarse = Button(self.__frame_btns, text="Registrarse", 
                        command= lambda: self.registrarse())
        btn_registrarse.grid(row=2, column=1, columnspan=1)

        btn_reiniciar_password = Button(self.__frame_btns, text="Reiniciar contraseña", 
                        command= lambda: crud.reiniciar_password())
        btn_reiniciar_password.grid(row=2, column=2, columnspan=1)


        
        self.__frame_btns.grid(row=2, column=0,columnspan=2)

        self.__container.pack(fill=BOTH)


        # Creo por default usuario admin
        try:    
            modulo_bd.generar_admin()
        except:
            print('Error al generar admin, posiblemente ya generado')

        self.__master.grab_set()
        self.__master.focus_force()
        self.__master.wait_window()



    
    def iniciar_sesion(self):
        usuario_name = self.__entry_usuario.get()
        password= bytes(self.__entry_password.get(),'utf-8')

        # encripto el password ingresado
        salt= b'aleaotorio'
        h = hashlib.pbkdf2_hmac('sha256',password, salt, 100)

        password_encriptado= h.hex()

        # print(usuario_name+ '  ' + str(password)+  '  ' +str(password_encriptado))

        
        self.__usuarios= modulo_bd.buscar_usuario(usuario_name = usuario_name, password= password_encriptado)

        if len(self.__usuarios)>0:
            self.__master.destroy() # Destruyo un Tk antes de iniciar el resto.
             
            # home_page = home.MyApp(usuarios[0].admin) # Recordar q es un iterable. (por eso el 0 entre corchetes)
            # home_page.mainloop()
        else:
            showinfo('-', 'Usuario o Contraseña ingresada incorrecta')
        # if length()
    
    def registrarse(self):
        formularios.Form_registrar_usuario(admin=False)

    def get_usuario(self):
        return self.__usuarios[0]







# app = Auth()
# app.mainloop()

