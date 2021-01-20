import sqlite3
import os
import globales
from peewee import *
import logging
import hashlib

# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

try:
    """
    Metodo para 
    Creacion de BD
    """
    db = SqliteDatabase(globales.db_name)
    class Base_model (Model):
        class Meta:
            database = db

    class Usuarios(Base_model):
        usuario_id=AutoField()
        usuario= CharField(unique=True, null=False)
        password= CharField(null=False)
        admin= BooleanField(null=False)

    class Insumos(Base_model):
        insumo_id = AutoField()
        descripcion = CharField(unique = True,null=False)
        codigo_unico = IntegerField(unique=True, null=False)
        activo = BooleanField(null=False)
        

    class Registros(Base_model):
        registro_id = AutoField()
        insumo_id = ForeignKeyField(Insumos)
        lote_partida = CharField(null=False)
        vencimiento = DateField(null=False)
        cantidad = IntegerField(null=False)


    db.connect()
    db.create_tables([Usuarios,Insumos,Registros])


except: 
    print('Error al crear bd')
            
##############################################################
################## CRUD INSUMOS ##############################
##############################################################
def alta_insumo(descripcion: 'Desc.',
        codigo_unico : 'Codigo unico de medicamento', 
        activo: 'activo/inactivo', 
        ):

    """
    Generacion de alta en BD
    """
    insumo_alta = Insumos()
    insumo_alta.descripcion = descripcion
    insumo_alta.activo = activo
    insumo_alta.codigo_unico =codigo_unico
    insumo_alta.save()


def modificar_insumo(descripcion:'Desc. Insumo', 
            codigo_unico : 'codigo_unico',activo: 'activo/inactivo',
            id : 'identificacion'):

    """
    Generacion de modificacion en BD
    """
    insumo_modificar = Insumos.update(descripcion=descripcion,
                                    codigo_unico=codigo_unico,
                                    activo=activo,
                                ).where(Insumos.insumo_id==id)
    insumo_modificar.execute()


def eliminar_insumo(codigo_unico): 
    insumo_eliminar = Insumos.get(Insumos.codigo_unico== codigo_unico)
    insumo_eliminar.delete_instance()


    """
    Generacion de baja en BD
    """  
    """
    sql ='DELETE FROM '+str(tabla)+ ' WHERE id=?'
    conexion=sqlite3.connect(str(self.__direccion)+ '\\'+str(self.__db_name))
    cursor = conexion.cursor()
    cursor.execute(sql,(id,))
    conexion.commit()
    cursor.close
    conexion.close
    """

def registros_insumo(self):   
    """
    Generacion de busqueda de todos los registros en BD
    """  
    """
    conexion=sqlite3.connect(str(self.__direccion)+ ''+str(self.__db_name))
    cursor = conexion.cursor()
    lista=cursor.execute('SELECT * FROM  'producto'')
        
    cursor.close
    conexion.close
    return lista
"""
def buscar_insumo(id):
    """
    Generacion de busqueda en BD
    """     
    insumos = Insumos().select().where(Insumos.insumo_id==id)
    return insumos

def buscar_insumo_by_codigo(codigo):
    """
    Generacion de busqueda en BD
    """     
    insumos = Insumos().select().where(Insumos.codigo_unico==codigo)
    return insumos

def buscar_insumo_all():
    """
    Generacion de busqueda en BD
    """     
    insumos = Insumos.select()
    return insumos
        
##############################################################
################## FIN CRUD INSUMOS ##########################
##############################################################
            
##############################################################
################## CRUD Registros ##############################
##############################################################
def alta_registro(
        codigo_insumo: 'Codigo Insumo.',
        lote_partida : 'lote_partida', 
        vencimiento,
        cantidad: '999', 
        ):

    """
    Generacion de alta en BD
    """
    insumo = buscar_insumo_by_codigo(codigo_insumo)

    registro_alta = Registros()
    registro_alta.insumo_id = insumo[0].insumo_id
    registro_alta.lote_partida = lote_partida
    registro_alta.vencimiento = vencimiento
    registro_alta.cantidad = cantidad
    registro_alta.save()


def modificar_registro(codigo_insumo:'codigo_insumo',
            lote_partida:'lote_partida', 
            vencimiento : 'vencimiento', cantidad: ' cantidad de libros',
            id : 'identificacion'):

    """
    Generacion de modificacion en BD
    """
    insumo = buscar_insumo_by_codigo(codigo_insumo)

    registro_modificar = Registros.update(lote_partida=lote_partida,
                                    vencimiento=vencimiento,
                                    cantidad=cantidad,
                                    insumo_id=insumo[0].insumo_id,
                                ).where(Registros.registro_id==id)
    registro_modificar.execute()


def eliminar_registro(id): 
    registro_eliminar = Registros.get(Registros.registro_id== id)
    registro_eliminar.delete_instance()


    """
    Generacion de baja en BD
    """  
    """
    sql ='DELETE FROM '+str(tabla)+ ' WHERE id=?'
    conexion=sqlite3.connect(str(self.__direccion)+ '\\'+str(self.__db_name))
    cursor = conexion.cursor()
    cursor.execute(sql,(id,))
    conexion.commit()
    cursor.close
    conexion.close
    """

def registros_registro(self):   
    """
    Generacion de busqueda de todos los registros en BD
    """  
    """
    conexion=sqlite3.connect(str(self.__direccion)+ ''+str(self.__db_name))
    cursor = conexion.cursor()
    lista=cursor.execute('SELECT * FROM  'producto'')
        
    cursor.close
    conexion.close
    return lista
"""
def buscar_registro(id):
    """
    Generacion de busqueda en BD
    """     
    registros = Registros().select().where(Registros.registro_id==id)
    return registros
        
def buscar_registros_all():
    """
    Generacion de busqueda en BD
    """     
    registros = Registros().select()
    return registros
##############################################################
################## FIN CRUD REGISTROS ##########################
##############################################################



##############################################################
################## CRUD Usuarios ##############################
##############################################################
def alta_usuario(usuario_name: 'usuario name.',
        password : 'password', 
        admin: 'admin/general', 
        ):

    """
    Generacion de alta en BD
    """
    usuario_alta = Usuarios()
    usuario_alta.usuario = usuario_name
    usuario_alta.password= password
    usuario_alta.admin = admin
    usuario_alta.save()


def actualizar_usuario(usuario_name:'usuario_name', 
                      password: ' contraseña',
                      admin : 'admin'):

    """
    Generacion de modificacion en BD
    """
    




    usuario_modificar = Usuarios.update(usuario=usuario_name,
                                        password=password,
                                        admin=admin
                                        ).where(Usuarios.usuario==usuario_name)
    usuario_modificar.execute()


def eliminar_usuario(usuario_name): 
    insumo_eliminar = Usuarios.get(Usuarios.usuario== usuario_name)
    insumo_eliminar.delete_instance()


#     """
#     Generacion de baja en BD
#     """  
#     """
#     sql ='DELETE FROM '+str(tabla)+ ' WHERE id=?'
#     conexion=sqlite3.connect(str(self.__direccion)+ '\\'+str(self.__db_name))
#     cursor = conexion.cursor()
#     cursor.execute(sql,(id,))
#     conexion.commit()
#     cursor.close
#     conexion.close
#     """

# def registros_insumo(self):   
#     """
#     Generacion de busqueda de todos los registros en BD
#     """  
#     """
#     conexion=sqlite3.connect(str(self.__direccion)+ ''+str(self.__db_name))
#     cursor = conexion.cursor()
#     lista=cursor.execute('SELECT * FROM  'producto'')
        
#     cursor.close
#     conexion.close
#     return lista
# """
def buscar_usuario(usuario_name,password):
    """
    Generacion de busqueda en BD
    """     
    usuarios= Usuarios().select().where(Usuarios.password==password,
                                        Usuarios.usuario== usuario_name)
    return usuarios




# def buscar_insumo_by_codigo(codigo):
#     """
#     Generacion de busqueda en BD
#     """     
#     insumos = Insumos().select().where(Insumos.codigo_unico==codigo)
#     return insumos

def buscar_usuarios_all():
    """
    Generacion de busqueda en BD
    """     
    usuarios = Usuarios.select()
    return usuarios
        
##############################################################
################## FIN CRUD Usuarios##########################
##############################################################



def generar_admin():
    # Creo por default usuario admin
    admin = Usuarios()
    admin.usuario = 'admin'
    admin.admin=True
    password = b'password'

    # encripto el password ingresado
    salt= b'aleaotorio'
    h = hashlib.pbkdf2_hmac('sha256',password, salt, 100)
    password_encriptado= h.hex()

    admin.password = password_encriptado
    admin.save()
