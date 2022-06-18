from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = {'nome', 'instituicao'}
        labels = {
            'nome':'Nome do curso',
            'instituicao':'Instituição de ensino'
        }

