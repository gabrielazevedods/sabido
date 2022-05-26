from django import forms
from .models import Aluno

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = {'nome', 'professor', 'carga_horaria', 'codigo_disciplina'}
        labels = {
            'nome':'Nome do aluno',
            'username':'Nome de Usuário',
            'dataNasc':'Data de Nascimento',
            'email':'Email'
        }
