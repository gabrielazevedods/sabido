from django.db import models
from django.core.files import File
import os
import urllib

# Create your models here.

class Lembrete(models.Model):

    titulo = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 250)
    imagem = models.URLField(max_length=300)
    arquivo = models.FileField()

    def __str__(self):
        return self.nome



