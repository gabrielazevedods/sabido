from django.db import models

# Create your models here.

class Disciplina(models.Model):
    nome = models.CharField(max_length = 50)
    professor = models.CharField(max_length = 50)
    carga_horaria = models.IntegerField()
    codigo_disciplina = models.CharField(max_length = 7)

    def __str__(self):
        return self.nome

class Compromisso(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.CharField(max_length = 100)
    data_compromisso = models.DateField()
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE)


