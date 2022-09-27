"""
Descripción: Lectura de datos para la conexión con la base de datos.
Autor: IDS.
"""
import configparser
import logging

class PropertiesReader():
    """
    Clase de lectura.
    """
    try:
        config = configparser.ConfigParser()
        config.read('app/Utils/ConfigFile.properties')
        db_host = config.get("db", "db_host")
        db_puerto = config.get("db", "db_puerto")
        db_name = config.get("db", "db_name")
        user = config.get("db", "user")
        password = config.get("db", "password")

    except RuntimeError:
        logging.exception(
            "Ocurrió un error con la conexión a la base de datos.")
