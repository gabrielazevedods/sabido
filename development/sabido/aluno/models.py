from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length = 100)
    dataNasc = models.DateField(null=True)
    email = models.CharField(max_length=256)
    senha = models.CharField(max_length=256)

    def __str__(self):
        return self.nome

