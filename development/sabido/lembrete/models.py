from django.db import models

# Create your models here.

class Lembrete(models.Model):

    titulo = models.CharField(max_length = 50)
    descricao = models.CharField(max_length = 250)
    imagem = models.URLField(max_length=300)

    def __str__(self):
        return self.nome



