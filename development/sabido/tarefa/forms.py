from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = {'nome', 'descricao', 'data_inicio_tarefa', 'data_fim_tarefa', 'projeto'}
        labels = {
            'nome':'Nome da tarefa',
            'descricao':'Descrição da tarefa',
            'data_inicio_tarefa':'Data de início da tarefa',
            'data_fim_tarefa':'Data de fim da tarefa',
            'projeto':'Projeto'
        }
        
    def __init__(self, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        self.fields['projeto'].empty_label = "Selecione um projeto"
        self.fields['descricao'].required = False
        self.fields['data_fim_tarefa'].required = False
                
    data_inicio_tarefa = forms.DateField(
            widget=forms.DateInput(format='%d/%m/%Y'),
            input_formats=('%d/%m/%Y', )
    )

    data_fim_tarefa = forms.DateField(
            widget=forms.DateInput(format='%d/%m/%Y'),
            input_formats=('%d/%m/%Y', )
    )

