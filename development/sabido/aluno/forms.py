from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = {'nome', 'dataNasc', 'email'}
        labels = {
            'nome':'Nome do aluno',
            'dataNasc':'Data de Nascimento',
            'email':'Email'
        }

    dataNasc = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y'),
        input_formats=('%d/%m/%Y', )
    )

