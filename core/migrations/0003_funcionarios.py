# Generated by Django 4.0.6 on 2022-08-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='funcionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='nome')),
                ('senha', models.IntegerField(verbose_name='senha')),
                ('funcao', models.CharField(max_length=20, verbose_name='funcao')),
            ],
        ),
    ]
