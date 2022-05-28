from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        # fields = '__all__'
        fields = {'nome', 'descricao', 'data_tarefa', 'disciplina'}
        labels = {
            'nome':'Nome da tarefa',
            'descricao':'Descrição do tarefa',
            'data_tarefa':'Data da tarefa',
            'disciplina':'Disciplina'
        }
        
    def __init__(self, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        self.fields['disciplina'].empty_label = "Selecione uma disciplina"
        self.fields['descricao'].required = False
            

