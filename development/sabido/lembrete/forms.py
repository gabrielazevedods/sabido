from django import forms
from .models import Lembrete

class LembreteForm(forms.ModelForm):
    class Meta:
        model = Lembrete
        fields = {'titulo', 'descricao', 'imagem'}
        labels = {
            'titulo':'Título do lembrete',
            'descricao':'Descrição do lembrete',
            'imagem':'Adicionar uma imagem',
        }

    def __init__(self, *args, **kwargs):
        super(LembreteForm, self).__init__(*args, **kwargs)
        self.fields['imagem'].required = False

