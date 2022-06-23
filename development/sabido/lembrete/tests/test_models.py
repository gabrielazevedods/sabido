from django.test import TestCase
from lembrete.models import Lembrete
import re
import datetime

class ModelsTestCase(TestCase):
    def test_validar_dados_lembrete(self):
        pattern = r'[^A-Za-z]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres alfabéticos
        pattern2 = r'[^0-9]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres numéricos
        pattern3 = r'[^A-Za-z0-9]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres alfanuméricos
        
        lembrete = Lembrete.objects.create(titulo = "Fórmula de Bhaskara", descricao = "Usada para equações de segundo grau")
        lembrete.save()

        alphabetic_str = re.sub(pattern, ' ', lembrete.titulo)
        self.assertEqual(lembrete.titulo, alphabetic_str)