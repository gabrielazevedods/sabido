from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = {'nome', 'username', 'dataNasc', 'email'}
        labels = {
            'nome':'Nome do aluno',
            'username':'Nome de Usuário',
            'dataNasc':'Data de Nascimento',
            'email':'Email'
        }
