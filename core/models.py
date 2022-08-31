from django.db import models

# Create your models here.

class percas(models.Model):
    nome = models.CharField('nome', max_length=20)
    descricao= models.CharField('descrição', max_length=40)
    valor_compra = models.FloatField('valor_compra')
    valor_venda = models.FloatField('valor_venda')

class admin(models.Model):
    nome = models.CharField('nome', max_length=30)
    senha = models.IntegerField('senha')
    name = models.ImageField( 'name' )

class funcionarios(models.Model):
    nome = models.CharField('nome', max_length=40)
    senha = models.IntegerField('senha')
    funcao= models.CharField('funcao', max_length=20)
    