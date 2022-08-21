from dataclasses import field
from django.forms import ModelForm
from .models import percas


class percasForm(ModelForm):
    class Meta:
        model = percas 
        fields = ['nome', 'descricao','valor_compra', 'valor_venda']