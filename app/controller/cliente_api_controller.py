"""
Descripción: Controlador de Cliente API.
Autor: IDS.
"""
from flask import Blueprint, request, jsonify
from flask_restx import Api, Resource, fields
from service.cliente_service import (add_client, list_clients, update_client,
                                     delete_cliente, get_client_by_id)

clients = Blueprint('api_i', __name__)
api_i = Api(clients, version='1.0', title='API DE CLIENTES',
            description='Api estandar para Clientes en una base de datos')

api = api_i.namespace('Clientes', description='Click para ver CRUD')

field_add = api.model('Resource', {
    'nombre': fields.String,
    'descripcion1': fields.String,
    'descripcion2': fields.String})


@api.route('/client/')
@api.doc(body=field_add)
class AgregarCliente(Resource):
    """
    Ruta crear contacto y dentro la función para agregar un nuevo contacto
    """

    def post(self):
        """
        Función Post
        """
        cliente = request.get_json()
        add_client(cliente)
        return jsonify(cliente)


@api.route('/clients/')
@api.doc(descripton="Enlista a los clientes de la Base de Datos")
class ListarClientes(Resource):
    """
    Funcion para leer lista de contactos dentro de la misma ruta anterior
    """

    def get(self):
        """
        Función Get
        """
        return jsonify(list_clients())


@api.route('/clients/<_id>/')
@api.doc(descripton="Busca a un cliente por medio de su ID")
class ClienteById(Resource):
    """
    Ruta para buscar un cliente por id
    """

    def get(self, _id):
        """
        Función Get
        """
        return jsonify(get_client_by_id(_id))


@api.route('/client/<_id>/')
@api.doc(body=field_add)
class ClienteUpdate(Resource):
    """
    Ruta de actualizar un contacto con su función determinada dentro
    """

    def put(self, _id):
        """
        Función Put
        """
        update_cliente = request.get_json()
        return jsonify(update_client(update_cliente, _id))


@api.route('/cliente/<_id>/')
@api.doc(descripton="Elimina a aun cliente buscado por ID")
class DeleteCliente(Resource):
    """
    Ruta para borrar contacto con su función de eliminar contacto.
    """

    def delete(self, _id):
        """
        Función Delete
        """
        return jsonify(delete_cliente(_id))
