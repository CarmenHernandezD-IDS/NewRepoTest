"""
Descripción: Cliente service.
Autor: IDS.
"""
from marshmallow import Schema
from model.cliente import Cliente
from repository.connect.cliente_connect import Conectar

class ClientsShema(Schema): # pylint: disable=too-few-public-methods
    """
    Clients Schema.
    """
    class Meta: # pylint: disable=too-few-public-methods
        """
        Clase Meta.
        """
        model: Cliente
        fields = ('id_logico', 'nombre', 'descripcion1', 'descripcion2',)
        load_instance = True

clientsShema = ClientsShema()

def add_client(client_data):
    """
    Método para registrar un usuario nuevo en la base de datos
    """
    cliente_nuevo = Cliente.insert(client_data)
    cliente_nuevo.execute() # pylint: disable=no-value-for-parameter
    Conectar.db.session_commit()
    return client_data

def get_client_by_id(_id):
    """
    Metodo para buscar cliente por id
    """
    cliente_byid = Cliente.select().where(Cliente.id_logico == _id)
    lista_id = []
    for row in cliente_byid: # pylint: disable=not-an-iterable
        # pylint: disable=consider-using-f-string
        impid = ("id_logico: {} nombre: {} descripcion1: {} descripcion2: {}".format(
            row.id_logico, row.nombre, row.descripcion1,
            row.descripcion2))
        cliente_byid.execute() # pylint: disable=no-value-for-parameter
        Conectar.db.session_commit()
        lista_id.append(impid)
    return lista_id

def list_clients():
    """
    Metodo para listar clientes
    """
    cliente_listar_todos = Cliente.select()
    lista = []
    for row in cliente_listar_todos:
        # pylint: disable=consider-using-f-string
        imp = ("id_logico: {} nombre: {} descripcion1: {} descripcion2: {}".format(
            row.id_logico, row.nombre, row.descripcion1, row.descripcion2))
        cliente_listar_todos.execute() # pylint: disable=no-value-for-parameter
        Conectar.db.session_commit()
        lista.append(imp)
    return lista

def update_client(client_data, _id):
    """
    Metodo para actualizar a un cliente
    """
    cliente_actualizar = Cliente.update(
        client_data).where(Cliente.id_logico == _id)
    cliente_actualizar.execute() # pylint: disable=no-value-for-parameter
    Conectar.db.session_commit()
    return client_data

def delete_cliente(_id):
    """
    Metodo para eliminar a un cliente
    """
    deletecliente = Cliente.delete().where(Cliente.id_logico == _id)
    deletecliente.execute() # pylint: disable=no-value-for-parameter
    Conectar.db.session_commit()
    return "Cliente eliminado"
