from django import forms
from .models import Cursos

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        # fields = '__all__'
        fields = {'nome', 'instituicao'}
        labels = {
            'nome':'Nome do curso',
            'instituicao':'Instituicao do curso'
        }