from django.test import TestCase
from tarefa.models import Tarefa
from disciplina.models import Disciplina
import re
import datetime

class ModelsTestCase(TestCase):
    def test_validar_dados_tarefa(self):
        pattern = r'[^A-Za-z0-9]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres alfanuméricos
        subject = Disciplina.objects.create(nome = "Engenharia de Software II", professor = "Taciano Silva", carga_horaria = 60, codigo_disciplina = "DCT2302")
        tarefa = Tarefa.objects.create(nome = "Develop Unit Tests", descricao = "Fazer os testes de unidades para o CRUD Tarefas", data_tarefa = datetime.datetime(2022, 6, 23), disciplina = subject)
        tarefa.save()
        alphanumeric_str = re.sub(pattern, ' ', tarefa.nome)
        self.assertEqual(tarefa.nome, alphanumeric_str)
        alphanumeric_str = re.sub(pattern, ' ', tarefa.descricao)
        self.assertEqual(tarefa.descricao, alphanumeric_str)
        sample_date = datetime.datetime(2022, 6, 20)
        self.assertEqual(type(tarefa.data_tarefa), type(sample_date))
        alphanumeric_str = re.sub(pattern, ' ', tarefa.disciplina.nome)
        self.assertEqual(tarefa.disciplina.nome, alphanumeric_str)

