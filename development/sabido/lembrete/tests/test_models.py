from django.test import TestCase
from lembrete.models import Lembrete
import re

class ModelsTestCase(TestCase):
    def test_validar_dados_lembrete(self):

        pattern = r'[^A-Za-z]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres alfabéticos
        
        lembrete = Lembrete.objects.create(titulo = "Fórmula de Bhaskara", descricao = "Usada para equações de segundo grau")
        lembrete.save()

        alphabetic_str = re.sub(pattern, ' ', lembrete.titulo)
        self.assertEqual(lembrete.titulo, alphabetic_str)

