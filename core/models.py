from django.db import models

# Create your models here.

class percas(models.Model):
    nome = models.CharField('nome', max_length=20)
    descricao= models.CharField('descrição', max_length=40)
    valor_compra = models.FloatField('valor_compra')
    valor_venda = models.FloatField('valor_venda')