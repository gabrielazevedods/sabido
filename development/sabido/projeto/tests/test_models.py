from django.test import TestCase
from disciplina.models import Disciplina
from projeto.models import Projeto
import re
import datetime

class ModelsTestCase(TestCase):
    def test_validar_dados_projeto(self):

        pattern = r'[^A-Za-z0-9]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres alfanuméricos
        pattern2 = r'[^0-9]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres numéricos
        pattern3 = r'[^a-zA-Zà-úÀ-Ú0-9]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres alfanuméricos com acentos
        
        subject = Disciplina.objects.create(nome = "Engenharia de Software II", professor = "Taciano Silva", carga_horaria = 60, codigo_disciplina = "DCT2302")
        projeto = Projeto.objects.create(nome = "SABIDO", descricao = "Desenvolver um app de auxílio acadêmico", coordenador = "Taciano Silva", carga_horaria = 60, data_inicio_projeto = datetime.datetime(2022, 4, 19), data_fim_projeto = datetime.datetime(2022, 7, 19), disciplina = subject)
        projeto.save()
        
        alphanumeric_str = re.sub(pattern, ' ', projeto.nome)
        self.assertEqual(projeto.nome, alphanumeric_str)

        alphanumeric_str = re.sub(pattern3, ' ', projeto.descricao)
        self.assertEqual(projeto.descricao, alphanumeric_str)

        alphanumeric_str = re.sub(pattern, ' ', projeto.coordenador)
        self.assertEqual(projeto.coordenador, alphanumeric_str)

        self.assertEqual(isinstance(projeto.carga_horaria, int), isinstance(60, int))

        sample_date = datetime.datetime(2022, 6, 20)
        self.assertEqual(type(projeto.data_inicio_projeto), type(sample_date))

        sample_date = datetime.datetime(2022, 7, 19)
        self.assertEqual(type(projeto.data_fim_projeto), type(sample_date))

        alphanumeric_str = re.sub(pattern3, ' ', projeto.disciplina.nome)
        self.assertEqual(projeto.disciplina.nome, alphanumeric_str)

