from django.db import models
from disciplina.models import Disciplina

# Create your models here.

class Tarefa(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.CharField(max_length = 100)
    data_tarefa = models.DateField()
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome

