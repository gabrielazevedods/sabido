from django import forms
from .models import KanbanToDo
from .models import KanbanDoing 
from .models import KanbanDone

class KanbanToDoForm(forms.ModelForm):
    class Meta:
        model = KanbanToDo
        # fields = '__all__'
        fields = {'tarefa'}
        labels = {
            'tarefa':'Tarefa'
        }
        
    def __init__(self, *args, **kwargs):
        super(KanbanToDoForm, self).__init__(*args, **kwargs)
        self.fields['tarefa'].empty_label = "Tarefa a ser alocada no Quadro Kanban To Do"




class KanbanDoingForm(forms.ModelForm):
    class Meta:
        model = KanbanDoing
        # fields = '__all__'
        fields = {'tarefa'}
        labels = {
            'tarefa':'Tarefa'
        }
        
    def __init__(self, *args, **kwargs):
        super(KanbanDoingForm, self).__init__(*args, **kwargs)
        self.fields['tarefa'].empty_label = "Tarefa a ser alocada no Quadro Kanban Doing"




class KanbanDoneForm(forms.ModelForm):
    class Meta:
        model = KanbanDone
        # fields = '__all__'
        fields = {'tarefa'}
        labels = {
            'tarefa':'Tarefa'
        }
        
    def __init__(self, *args, **kwargs):
        super(KanbanDoneForm, self).__init__(*args, **kwargs)
        self.fields['tarefa'].empty_label = "Tarefa a ser alocada no Quadro Kanban Done"



