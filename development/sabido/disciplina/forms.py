from django import forms
from .models import Disciplina

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        # fields = '__all__'
        fields = {'nome', 'professor', 'carga_horaria', 'codigo_disciplina'}
        labels = {
            'nome':'Nome da disciplina',
            'professor':'Professor da disciplina',
            'carga_horaria':'Carga horária da disciplina',
            'codigo_disciplina':'Código da disciplina'
        }
