from django.db import models
from disciplina.models import Disciplina

# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 50)
    coordenador = models.CharField(max_length = 50)
    carga_horaria = models.IntegerField()
    data_inicio_projeto = models.DateField()
    data_fim_projeto = models.DateField()
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome

