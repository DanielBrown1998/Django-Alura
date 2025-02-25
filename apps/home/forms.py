from django import forms
from apps.home.models import Fotografia

class FotografiaForm(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude= ['publicada']
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'categoria': 'Categoria',
            'imagem': 'Imagem',
            'data_fotografia': 'Data da Fotografia',
            'legenda': 'Legenda',
            'usuario': 'Usuário',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateTimeInput(
                attrs={
                    'class': 'form-control', 
                    'type': 'date'
                    }, 
                format='%Y-%m-%d'
                ),
        }


# Compare this snippet from apps/home/models.py: