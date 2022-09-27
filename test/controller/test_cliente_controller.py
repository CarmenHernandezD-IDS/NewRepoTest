"""
Descripción: Test cliente controller
Autor: IDS.
"""

import sys
from unittest import main, TestCase, mock
sys.path.append(
    r'.\app')
from controller import cliente_api_controller # pylint: disable=wrong-import-position

resp_espe = {
    "nombre": "Luis",
    "descripcion1": "Hombre",
    "descripcion2": "Feliz"
}

class MyTestCase(TestCase):
    """
    Clase MyTestCase
    """
    @mock.patch("controller.cliente_api_controller.ListarClientes.get")
    def test_clientes(self, mock_requests):
        """
        Método test cliente
        """
        mock_responde = mock.MagicMock()
        mock_responde.text = """
        {
            "nombre" : "Luis", "descripcion1" : "Hombre", descripcion2" : "Feliz"
        }
        """
        mock_requests.return_value = mock_responde.text
        lis_cli = cliente_api_controller.ListarClientes.get() # pylint: disable=no-value-for-parameter
        self.assertEqual(lis_cli, mock_requests.return_value)

    @mock.patch("controller.cliente_api_controller.AgregarCliente.post")
    def test_add_client(self, mock_requests):
        """
        Método test add cliente
        """
        mock_responde = mock.MagicMock()
        mock_responde.text = """
        {
            "cliente añadido"
        }
        """
        mock_requests.retunr_value = mock_responde.text
        addcli = cliente_api_controller.AgregarCliente.post() # pylint: disable=no-value-for-parameter
        self.assertEqual(addcli, mock_requests.return_value)

    @mock.patch("controller.cliente_api_controller.ClienteById.get")
    def test_client_by_id(self, mock_requests):
        """
        Método test cliente by id
        """
        mock_responde = mock.MagicMock()
        mock_responde.text = """
        {
            "id_logico" : "1", "nombre" : "Luis", "descripcion1" : "Hombre", descripcion2" : "Feliz"
        }
        """
        mock_requests.return_value = mock_responde.text
        byidcli = cliente_api_controller.ClienteById.get(1) # pylint: disable=no-value-for-parameter
        self.assertEqual(byidcli, mock_requests.return_value)

    @mock.patch("controller.cliente_api_controller.ClienteUpdate.put")
    def test_client_update(self, mock_requests):
        """
        Método test cliente update
        """
        mock_responde = mock.MagicMock()
        mock_responde.text = """
        {
            "nombre" : "Enrique", "descripcion1" : "Hombre", descripcion2" : "Casado"
        }
        """
        mock_requests.return_value = mock_responde.text
        updacli = cliente_api_controller.ClienteUpdate.put(1) # pylint: disable=no-value-for-parameter
        self.assertEqual(updacli, mock_requests.return_value)

    @mock.patch("controller.cliente_api_controller.DeleteCliente.delete")
    def test_delete_cliente(self, mock_requests):
        """
        Método test delete cliente
        """
        mock_responde = mock.MagicMock()
        mock_responde.text = """
        {
            Cliente eliminado
        }
        """
        mock_requests.return_value = mock_responde.text
        decli = cliente_api_controller.DeleteCliente.delete(1) # pylint: disable=no-value-for-parameter
        self.assertEqual(decli, mock_requests.return_value)

if __name__ == '__main__':
    main()
