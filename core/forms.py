from dataclasses import field, fields
from pyexpat import model
from django.forms import ModelForm
from .models import percas, funcionarios 




class percasForm(ModelForm):
    class Meta:
        model = percas 
        fields = ['nome', 'descricao','valor_compra', 'valor_venda']
class funcionariosForm(ModelForm):
    class Meta:
        model = funcionarios
        fields= ['nome', 'senha', 'funcao']


