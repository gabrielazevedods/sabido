from django.test import TestCase

class ViewsTestCase(TestCase):
    def test_aluno_list_loads_properly(self):
        response = self.client.get('http://localhost:8000/aluno/list/')
        self.assertEqual(response.status_code, 200)

    def test_aluno_create_loads_properly(self):
        response = self.client.get('http://localhost:8000/aluno/')
        self.assertEqual(response.status_code, 200)

