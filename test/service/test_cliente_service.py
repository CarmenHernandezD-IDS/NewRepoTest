"""
Descripción: Test cliente service
Autor: IDS.
"""
import sys
sys.path.append(
r'.\app')
from unittest import main, TestCase, mock # pylint: disable=wrong-import-position
from service import cliente_service  # pylint: disable=wrong-import-position

class ServiceTest(TestCase):
    """
    Clase Service Test
    """
    @mock.patch("service.cliente_service.add_client")
    def test_add(self, mock_requests):
        """
        Método test add
        """
        mock_response = mock.MagicMock()
        mock_response.text = """
        {
            "nombre" : "Gerald", "descripcion1" : "Hombre", "descripcion2" : "feliz"
        }
        """
        mock_requests.return_value = mock_response.text
        add_c = cliente_service.add_client(mock_response.text)
        self.assertEquals(add_c, mock_requests.return_value) # pylint: disable=deprecated-method

    @mock.patch("service.cliente_service.get_client_by_id")
    def test_list_by_id(self, mock_requests):
        """
        Método test listar
        """
        mock_respuesta = mock.MagicMock()
        mock_respuesta.text = """
        {
            "id_logico" : "1", "nombre" : "Gerald", "descripcion1" : "Hombre", "descripcion2" : "feliz"
        }
        """
        mock_requests.return_value = mock_respuesta.text
        lis_id_c = cliente_service.get_client_by_id(1)
        self.assertEqual(lis_id_c, mock_requests.return_value)

    @mock.patch("service.cliente_service.list_clients")
    def test_list(self, mock_resquests):
        """
        Método test listar
        """
        mock_respuesta = mock.MagicMock()
        mock_respuesta.text = """
        {
            "id_logico" : "1", "nombre" : "Gerald", "descripcion1" : "Hombre", "descripcion2" : "feliz"
        }
        """
        mock_resquests.return_value = mock_respuesta.text
        lis_c = cliente_service.list_clients()
        self.assertEqual(lis_c, mock_resquests.return_value)

    @mock.patch("service.cliente_service.update_client")
    def test_update(self, mock_requests):
        """
        Método test update
        """
        mock_respuesta = mock.MagicMock()
        mock_respuesta.text = """
        {
            "id_logico" : "1", "nombre" : "Albert", "descripcion1" : "Hombre", "descripcion2" : "feliz"
        }
        """
        data = """
        {
            "nombre" : "Albert", "descripcion1" : "Hombre", "descripcion2" : "feliz"
        }
        """
        mock_requests.return_value = mock_respuesta.text
        up_cl = cliente_service.update_client(data, 1)
        self.assertEqual(up_cl, mock_requests.return_value)

    @mock.patch("service.cliente_service.delete_cliente")
    def test_delete(self, mock_requests):
        """
        Método test delete
        """
        mock_respuesta = mock.MagicMock()
        mock_respuesta.text = """
        {
            "Cliente eliminado"
        }
        """
        mock_requests.return_value = mock_respuesta.text
        del_cl = cliente_service.delete_cliente(1)
        self.assertEqual(del_cl, mock_requests.return_value)

if __name__ == '__main__':
    main()
