"""
Descripción: Módulo inicial, despliegue de la aplicación.
Autor: IDS.
"""

#  Importamos la libreria flask
from flask import Flask
from controller.cliente_api_controller import clients
from repository.connect.cliente_connect import Conectar

#  Llamamos a nuestra app de Flask
app = Flask(__name__)
#  Clients que importamos de Controller
app.register_blueprint(clients)

Conectar()

if __name__ == "__main__":
    app.run(debug=True)
