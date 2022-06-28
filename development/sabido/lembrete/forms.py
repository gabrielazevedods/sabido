from django import forms
from .models import Lembrete

class LembreteForm(forms.ModelForm):
    class Meta:
        model = Lembrete
        fields = {'titulo', 'descricao', 'imagem', 'arquivo'}
        labels = {
            'titulo':'Título do lembrete',
            'descricao':'Descrição do lembrete',
            'imagem':'Adicionar uma imagem',
            'arquivo':'Adicionar um arquivo'
        }

    def __init__(self, *args, **kwargs):
        super(LembreteForm, self).__init__(*args, **kwargs)
        self.fields['imagem'].required = False
        self.fields['arquivo'].required = False
