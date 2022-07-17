from django.db import models
from projeto.models import Projeto

# Create your models here.

class Tarefa(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.CharField(max_length = 100)
    data_inicio_tarefa = models.DateField()
    data_fim_tarefa = models.DateField()
    projeto = models.ForeignKey(Projeto, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome

