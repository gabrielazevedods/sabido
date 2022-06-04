from django.db import models
from tarefa.models import Tarefa

# Create your models here.

class KanbanToDo(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete = models.CASCADE)

class KanbanDoing(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete = models.CASCADE)
  
class KanbanDone(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete = models.CASCADE)


   

