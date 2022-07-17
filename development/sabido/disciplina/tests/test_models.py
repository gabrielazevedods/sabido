from django.test import TestCase
from disciplina.models import Disciplina
import re

class ModelsTestCase(TestCase):
    def test_validar_dados_disciplina(self):
        pattern = r'[^A-Za-z]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres alfabéticos
        pattern2 = r'[^0-9]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres numéricos
        pattern3 = r'[^A-Za-z0-9]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres alfanuméricos
        
        disciplina = Disciplina.objects.create(nome = "Engenharia de Software II", professor = "Taciano", carga_horaria = 60, codigo_disciplina = "DCT2302")
        disciplina.save()

        alphabetic_str = re.sub(pattern, ' ', disciplina.nome)
        self.assertEqual(disciplina.nome, alphabetic_str)

        alphabetic_str = re.sub(pattern, ' ', disciplina.professor)        
        self.assertEqual(disciplina.professor, alphabetic_str)

        self.assertEqual(isinstance(disciplina.carga_horaria, int), isinstance(60, int))

        alphanumeric_str = re.sub(pattern3, ' ', disciplina.codigo_disciplina)
        self.assertEqual(disciplina.codigo_disciplina, alphanumeric_str)


