from django import forms
from .models import Compromisso

class CompromissoForm(forms.ModelForm):
    class Meta:
        model = Compromisso
        # fields = '__all__'
        fields = {'nome', 'descricao', 'data_compromisso', 'disciplina'}
        labels = {
            'nome':'Nome do compromisso',
            'descricao':'Descrição do compromisso',
            'data_compromisso':'Data do compromisso',
            'disciplina':'Disciplina'
        }

    def __init__(self, *args, **kwargs):
        super(CompromissoForm, self).__init__(*args, **kwargs)
        self.fields['disciplina'].empty_label = "Selecione uma disciplina"
        self.fields['descricao'].required = False

