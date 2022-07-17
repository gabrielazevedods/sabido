from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = {'nome', 'descricao', 'coordenador', 'carga_horaria', 'data_inicio_projeto', 'data_fim_projeto', 'disciplina'}
        labels = {
            'nome':'Nome do projeto',
            'descricao':'Descrição do projeto',
            'coordenador':'Coordenador do projeto',
            'carga_horaria':'Carga-Horária do projeto', 
            'data_inicio_projeto':'Data de início do projeto',
            'data_fim_projeto':'Data de fim do projeto',
            'disciplina':'Disciplina'
        }
        
    def __init__(self, *args, **kwargs):
        super(ProjetoForm, self).__init__(*args, **kwargs)
        self.fields['disciplina'].empty_label = "Selecione uma disciplina"
        self.fields['descricao'].required = False
        self.fields['data_fim_projeto'].required = False
                
    data_inicio_projeto = forms.DateField(
            widget=forms.DateInput(format='%d/%m/%Y'),
            input_formats=('%d/%m/%Y', )
    )

    data_fim_projeto = forms.DateField(
            widget=forms.DateInput(format='%d/%m/%Y'),
            input_formats=('%d/%m/%Y', )
    )

