from django.test import TestCase
from tarefa.models import Tarefa
from projeto.models import Projeto
import re
import datetime

class ModelsTestCase(TestCase):
    def test_validar_dados_tarefa(self):
        pattern = r'[^A-Za-z0-9]+' # Padrão de expressão regular para limitar o usuário a inserir somente caracteres alfanuméricos
        subject = Projeto.objects.create(nome = "SABIDO", descricao = "Desenvolvimento do software SABIDO como projeto final da disciplina", coordenador = "Taciano Silva", carga_horaria = 60, data_inicio_projeto = datetime.datetime(2022, 4, 19), data_fim_projeto = datetime.datetime(2022, 7, 19), disciplina = "Engenharia de Software II")
        tarefa = Tarefa.objects.create(nome = "Develop Unit Tests", descricao = "Fazer os testes de unidades para o CRUD de Tarefas", data_inicio_tarefa = datetime.datetime(2022, 6, 23), data_fim_tarefa = datetime.datetime(2022, 6, 26), projeto = subject)
        tarefa.save()
        alphanumeric_str = re.sub(pattern, ' ', tarefa.nome)
        self.assertEqual(tarefa.nome, alphanumeric_str)
        alphanumeric_str = re.sub(pattern, ' ', tarefa.descricao)
        self.assertEqual(tarefa.descricao, alphanumeric_str)
        sample_date = datetime.datetime(2022, 6, 20)
        self.assertEqual(type(tarefa.data_inicio_tarefa), type(sample_date))
        sample_date = datetime.datetime(2022, 7, 19)
        self.assertEqual(type(tarefa.data_fim_tarefa), type(sample_date))
        alphanumeric_str = re.sub(pattern, ' ', tarefa.projeto.nome)
        self.assertEqual(tarefa.projeto.nome, alphanumeric_str)

