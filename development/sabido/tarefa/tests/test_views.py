from django.test import TestCase

class ViewsTestCase(TestCase):
    def test_tarefa_list_loads_properly(self):
        response = self.client.get('http://localhost:8000/tarefa/list/')
        self.assertEqual(response.status_code, 200)

    def test_tarefa_create_loads_properly(self):
        response = self.client.get('http://localhost:8000/tarefa/')
        self.assertEqual(response.status_code, 200)

