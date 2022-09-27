"""
Descripción: Modelo Cliente.
Autor: IDS.
"""
from marshmallow import Schema, fields
from peewee import AutoField, TextField, Model, SqliteDatabase
from utils.python_properties_reader import PropertiesReader


class Cliente(Model):
    """
    Estructura de la tabla.
    """
    id_logico = AutoField()
    nombre = TextField()
    descripcion1 = TextField()
    descripcion2 = TextField()

    class Meta:
        """
        Clase Meta
        """
        db = SqliteDatabase(PropertiesReader.db_name)
        database = db


class ClientSchema(Schema):
    """
    Clase ClientSchema
    """
    _id_logico = fields.Int(dump_only=True)
    _nombre = fields.Str(required=True)
    _descripcion1 = fields.Str(required=True)
    _descripcion2 = fields.Str(required=True)

    @property
    def _id_logico(self):
        return self._id_logico

    @_id_logico.setter
    def _id_logico(self, id_logico):
        self._id_logico = id_logico

    @property
    def _nombre(self):
        return self._nombre

    @_nombre.setter
    def _nombre(self, nombre):
        self._nombre = nombre

    @property
    def _descripcion1(self):
        return self._descripcion1

    @_descripcion1.setter
    def _descripcion1(self, descripcion1):
        self._descripcion1 = descripcion1

    @property
    def _descripcion2(self):
        return self._descripcion2

    @_descripcion2.setter
    def _descripcion2(self, descripcion2):
        self._descripcion2 = descripcion2

clientSchema = ClientSchema()
