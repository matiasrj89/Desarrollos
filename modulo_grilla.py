from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import sqlite3
import os
import globales as gbl
from modulo_bd import *

    
def conectar (grilla,table_name):
    """
    Funcion que se encarga de conectar
    una  grilla con la base de datos.
    Parametro:
    grilla: objeto Treeview que se conectara a la BD.
    """
    
    conexion=sqlite3.connect(str(gbl.direccion)+ '\\'+str(gbl.db_name))
    cursor = conexion.execute("SELECT name FROM pragma_table_info('"+table_name+"')")
    lista_columnas = []
    
    for registro in cursor:
        lista_columnas.append(registro[0])  
        # print (x)  

    if table_name=='registros' and 'insumo_id' in lista_columnas:
        indice_aux=lista_columnas.index('insumo_id')
        lista_columnas[indice_aux]= 'descripcion del insumo'
 

    #Set grilla
    grilla['columns'] = tuple(lista_columnas)
    
    #Format columnas
    grilla.column("#0", width=0, stretch=NO)
    
    for x in range(len(lista_columnas)):
        grilla.column(lista_columnas[x], anchor =CENTER, minwidth=120)


    #Heading (Encabezado)
    grilla.heading("#0", text= '', anchor=W)
    
    for x in range(len(lista_columnas)):
        grilla.heading(lista_columnas[x],text=lista_columnas[x],anchor =CENTER)

    #Agregando la info
    registros = Insumos()
    registros = registros.select()
    # cursor=conexion.execute("SELECT * FROM '"+gbl.table_name+"'") 
    
    index = 0
    for registro in registros:
        
        grilla.insert(parent='', index='end', iid=index, text="", values=registro)
        index+=1

    # grilla.grid(row=0, column=0, sticky=W)
    # self.__frame.grid(row=0, column=0, sticky=W)

    
    cursor.close
    conexion.close


def actualizar_registros(grilla):
    """
    Funcion que se encarga de actualizar
    los registros de una  grilla con 
    respecto a una base de datos.
    Parametro:
    grilla: objeto Treeview que se 
    actualizara respecto a la BD.
    """
    #Agregando la info
    registros = Registros.select(Registros,Insumos).join(Insumos)
    #Limpio la grilla
    for row in grilla.get_children():
        grilla.delete(row)

    index = 0
    for registro in registros:
        print(registro)
        print('registro')
        
     

        grilla.insert(parent='', index='end', iid=index, text="", values=[registro.registro_id,
                                                                          registro.insumo_id.descripcion,
                                                                          registro.lote_partida,
                                                                          registro.vencimiento,
                                                                          registro.cantidad])
        index+=1
    
    # cursor.close
    # conexion.close

def item_selected(grilla):
    """
    Funcion que detecta el registro
    seleccionado en una grilla.
    Parametro:
    grilla: objeto Treeview sobre el que se trabajara.
    """
    if (len(grilla.selection()) != 0):
        for x in grilla.selection():
            registro = grilla.item(x)['values'] 
    else :
        registro = None

    
    return  registro



def actualizar_insumos(grilla):
    """
    Funcion que se encarga de actualizar
    los registros de una  grilla con 
    respecto a una base de datos.
    Parametro:
    grilla: objeto Treeview que se 
    actualizara respecto a la BD.
    """
    #Agregando la info
    insumos = Insumos.select()
    #Limpio la grilla
    for row in grilla.get_children():
        grilla.delete(row)
    

    index = 0
    for insumo in insumos:
        print (insumo)
        grilla.insert(parent='', index='end', iid=index, text="", values=[insumo.insumo_id,
                                                                          insumo.descripcion,
                                                                          insumo.codigo_unico,
                                                                          insumo.activo])
        index+=1
    
    # cursor.close
    # conexion.close



def item_selected_insumos(grilla):
    """
    Funcion que detecta el registro
    seleccionado en una grilla.
    Parametro:
    grilla: objeto Treeview sobre el que se trabajara.
    """
    if (len(grilla.selection()) != 0):
        for x in grilla.selection():
            insumo = grilla.item(x)['values'] 
    else :
        insumo = None

    
    return  insumo


def actualizar_usuarios(grilla):
    """
    Funcion que se encarga de actualizar
    los registros de una  grilla con 
    respecto a una base de datos.
    Parametro:
    grilla: objeto Treeview que se 
    actualizara respecto a la BD.
    """
    #Agregando la info
    usuarios = Usuarios.select()
    #Limpio la grilla
    for row in grilla.get_children():
        grilla.delete(row)

    index = 0
    for usuario in usuarios:
        print(usuario)
        print('usuario')
        
     

        grilla.insert(parent='', index='end', iid=index, text="", values=[usuario.usuario_id,
                                                                          usuario.usuario,
                                                                          usuario.password,
                                                                          usuario.admin,
                                                                          ])
        index+=1
    


def item_selected_usuarios(grilla):
    """
    Funcion que detecta el registro
    seleccionado en una grilla.
    Parametro:
    grilla: objeto Treeview sobre el que se trabajara.
    """
    if (len(grilla.selection()) != 0):
        for x in grilla.selection():
            usuario = grilla.item(x)['values'] 
    else :
        usuario = None

    
    return  usuario