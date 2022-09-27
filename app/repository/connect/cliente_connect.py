"""
Descripción: Módulo cliente connect.
Autor: IDS.
"""
import logging
from peewee import SqliteDatabase
from utils.python_properties_reader import PropertiesReader
from model.cliente import Cliente

class Conectar():
    """
    Conexión a la base de datos.
    """
    try:
        db = SqliteDatabase(PropertiesReader.db_name)
        db.connect()
        print("\n" + "Conexión establecida correctamente...")
        db.create_tables([Cliente])
        print("Tabla creada correctamente..." + "\n")

    except RuntimeError:
        logging.exception(
            "Ocurrió un error en la conexión con la base de datos.")
