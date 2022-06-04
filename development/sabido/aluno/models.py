from django.db import models
# from django import forms
from django.conf import settings
# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(max_length = 100)
    dataNasc = models.DateField(null=True)
    email = models.CharField(max_length=256)

    def __str__(self):
        return self.nome

