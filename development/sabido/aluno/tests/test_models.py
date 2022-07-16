from django.test import TestCase
from aluno.models import Aluno
import re
import datetime

class ModelsTestCase(TestCase):
    def test_validar_dados_aluno(self):
        pattern = r'[^A-Za-z]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres alfabéticos
        pattern2 = r'/^[a-z0-9.]+@[a-z0-9]+\.[a-z]+\.([a-z]+)?$/i;' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres numéricos
        pattern3 = r'[^A-Za-z0-9]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres alfanuméricos
        
        aluno = Aluno.objects.create(nome = "Danrley Daniel Moreira Sales", dataNasc = datetime.datetime(2000, 9, 6), email="danrleydaniel21@gmail.com")
        aluno.save()

        alphabetic_str = re.sub(pattern, ' ', aluno.nome)
        self.assertEqual(aluno.nome, alphabetic_str)

        sample_date = datetime.datetime(2022, 6, 20)
        self.assertEqual(type(aluno.dataNasc), type(sample_date))

        sample_email = re.sub(pattern2, ' ', aluno.email)
        self.assertEqual(aluno.email, sample_email)