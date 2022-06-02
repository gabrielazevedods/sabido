from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length = 50)
    instituicao = models.CharField(max_length = 50)
    

    def __str__(self):
        return self.nome

