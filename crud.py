
from tkinter.messagebox import *
import formularios
import modulo_grilla as mdgrilla
import sqlite3
import os
import globales as gbl
################ Definicion de funciones#############################

#####################################################################
################### CRUD REGISTROS###################################
#####################################################################
######################Sorpresa#######################################
# def sorpresa():

#     R = random.randint(0, 0xFF)
#     G = random.randint(0, 0xFF)
#     B = random.randint(0, 0xFF)
#     color = (R, G, B)
#     colorstr = "#%02x%02x%02x" % color
#     container.configure(background=colorstr)

######################  actualizar_registro  #######################################
def actualizar_registro(grilla):
   """
   Funcion que se encarga de actualizar la grilla
   """
   mdgrilla.actualizar_registros(grilla)
    
######################  Guardar_registro  #######################################
def guardar_registro(grilla):
    """
    Funcion adicional para guardar info.
    """
    showinfo('guardar','guardar')
    actualizar_registro(grilla)

######################  Alta_registro  #######################################
def alta_registro(grilla):
    """
    Funcion que inicializa el proceso de alta 
    """
    try:
        formularios.FormAlta_registro()  
        actualizar_registro(grilla)     
        
    except :
        showinfo('Error', 
                'Se ha producido un error al intentar abrir' 
                ' la ventana de altas')
    
    
    # modulobd.crearBD()

######################  Modificar_registro  #######################################
def modificar_registro(grilla):
    """
    Funcion que inicializa el proceso de modificacion 
    """
    registro = mdgrilla.item_selected(grilla)
    
    if registro != None:

        try:
            fm_modificar = formularios.FormModificar_registro(registro)
            actualizar_registro(grilla)
        except:
            showinfo('Error', ' Se ha producido un error al intentar' 
                    ' abrir la ventana de Modificacion')
    
    else:
        showinfo('Notificacion', 'Por favor, seleccione el item a modificar')
    
    

######################  Baja_registro  #######################################
def baja_registro(grilla):
    """
    Funcion que inicializa el proceso de baja 
    """
    try:
        fm_baja = formularios.FormBaja_registro()   
        actualizar_registro(grilla)
        
    except :
        showinfo('Error', ' Se ha producido un error al intentar' 
                ' abrir la ventana de Baja') 
          
######################  Buscar  #######################################
def buscar_registro(grilla):
    """
    Funcion que inicializa el proceso de busqueda 
    """
    try:
        fm_buscar= formularios.FormBuscar_registro()
        actualizar_registro(grilla)
    except :
        showinfo('Error', ' Se ha producido un error al intentar'
                ' abrir la ventana de Busqueda') 
    

#####################################################################
################### FIN CRUD REGISTROS###############################
#####################################################################

#####################################################################
################## CRUD INSUMOS######################################
#####################################################################

######################  actualizar_insumo  #######################################
def actualizar_insumo(grilla):
   """
   Funcion que se encarga de actualizar la grilla
   """
   mdgrilla.actualizar_insumos(grilla)
    
######################  Guardar_insumo  #######################################
def guardar_insumo(grilla):
    """
    Funcion adicional para guardar info.
    """
    showinfo('guardar','guardar')
    actualizar_insumo(grilla)  
######################  Alta_insumo  #######################################
def alta_insumo(grilla):
    """
    Funcion que inicializa el proceso de alta 
    """
    try:
        formularios.FormAlta_insumo()  
        actualizar_insumo(grilla)  
        
    except :
        showinfo('Error', 
                'Se ha producido un error al intentar abrir' 
                ' la ventana de altas')
    
    
    # modulobd.crearBD()

######################  Modificar_insumo  #######################################
def modificar_insumo(grilla):
    """
    Funcion que inicializa el proceso de modificacion 
    """
    insumo = mdgrilla.item_selected_insumos(grilla)
    
    if insumo != None:

        try:
            fm_modificar = formularios.FormModificar_insumo(insumo)
            actualizar_insumo(grilla)  
        except:
            showinfo('Error', ' Se ha producido un error al intentar' 
                    ' abrir la ventana de Modificacion')
    
    else:
        showinfo('Notificacion', 'Por favor, seleccione el item a modificar')
    
    

######################  Baja_insumo  #######################################
def baja_insumo(grilla):
    """
    Funcion que inicializa el proceso de baja 
    """
    try:
        fm_baja = formularios.FormBaja_insumo()   
        actualizar_insumo(grilla)  
        
    except :
        showinfo('Error', ' Se ha producido un error al intentar' 
                ' abrir la ventana de Baja') 
          
######################  Buscar_insumo  #######################################
def buscar_insumo(grilla):
    """
    Funcion que inicializa el proceso de busqueda 
    """
    try:
        fm_buscar= formularios.FormBuscar_insumo()
        actualizar_insumo(grilla)  
    except :
        showinfo('Error', ' Se ha producido un error al intentar'
                ' abrir la ventana de Busqueda') 
    


#####################################################################
################### FIN CRUD INSUMOS###############################
#####################################################################

#####################################################################
################## CRUD USUARIOS######################################
######################################################################

######################  actualizar_usuario #######################################
def actualizar_usuarios(grilla):
   """
   Funcion que se encarga de actualizar la grilla
   """
   mdgrilla.actualizar_usuarios(grilla)
   
######################  alta_usuario #######################################
def alta_usuario(grilla):
    """
    Funcion que inicializa el proceso de baja 
    """
    try:
        formularios.Form_registrar_usuario(admin=True)  
        actualizar_usuarios(grilla)  
        
    except :
        showinfo('Error', ' Se ha producido un error al intentar' 
                ' abrir la ventana de Baja') 

######################  alta_usuario #######################################
def editar_perfil_usuario(grilla):
    """
    Funcion que inicializa el proceso de modificacion 
    """
    usuario = mdgrilla.item_selected_usuarios(grilla)
    
    if usuario != None:

        try:
            formularios.Form_editar_perfil_usuario(usuario)
            actualizar_usuarios(grilla)  
        except:
            showinfo('Error', ' Se ha producido un error al intentar' 
                    ' abrir la ventana de edicion de perfil')
    
    else:
        showinfo('Notificacion', 'Por favor, seleccione el item a modificar')




######################  Baja_usuario #######################################
def baja_usuario(grilla):
    """
    Funcion que inicializa el proceso de baja 
    """
    try:
        formularios.Form_baja_usuario()   
        actualizar_usuarios(grilla)  
        
    except :
        showinfo('Error', ' Se ha producido un error al intentar' 
                ' abrir la ventana de Baja') 


######################  reiniciar password #######################################
def reiniciar_password():
    """
    Funcion que inicializa el proceso de reiniciar password
    """
    try:
        formularios.Form_reiniciar_password()   
        
        
    except :
        showinfo('Error', ' Se ha producido un error al intentar' 
                ' abrir la ventana de Baja') 
          
        

#####################################################################
################### FIN CRUD USUARIOS###############################
#####################################################################