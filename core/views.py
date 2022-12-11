import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import percasForm, funcionariosForm
from .models import percas, funcionarios
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'index.html',{'nome':'IFRN'})
def adiministrador(request):
    return render(request, 'adiministrador.html',{'nome':'adiministrador'})
def moto(request):
    return render(request, 'moto.html',{'nome':'moto'})    
def progresso(request):
    return render(request, 'progresso.html',{'nome':'progresso'})
def lista_percas(request):
    perca = percas.objects.all()
    contexto ={
        'todas_percas': perca
    }
    return render(request, 'lista_percas.html', contexto)     
def percas_cadastrar(request):
    form = percasForm(request.POST or None )
    if form.is_valid():
       form.save()
       return redirect('lista_percas')
    contexto ={
        'form_percas': form
    }
    return render(request, 'percas_cadastrar.html',contexto) 

def editar_percas(request, id):
    perca = percas.objects.get(pk=id)

    form = percasForm(request.POST or None, instance=perca)

    if form.is_valid():
        form.save()
        return redirect('lista_percas')

    contexto ={
        'form_percas': form
    }   
    return render(request, 'percas_cadastrar.html',contexto)
    
def remover_percas(request, id):
    perca = percas.objects.get(pk=id)
    perca.delete()
    return redirect('lista_percas')   
def adimin(request):
    return render(request, 'admin.html',{'nome':'admin'})
def lista_funcionarios(request):
    funcionario = funcionarios.objects.all()
    contexto={
        'todos_funcionarios': funcionario
    }
    return render(request, 'funcionarios.html',contexto)    
def cadastrar_funcionario(request):
    form = funcionariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_funcionarios')
    contexto={
        'form_funcionarios':form
    }
    return render(request,'funcionario_cadastrar.html', contexto)
def editar_funcionario(request, id):
    funcionario = funcionarios.objects.get(pk=id)
    form=funcionariosForm(request.POST or None, instance=funcionario)
    if form.is_valid():
        form.save()
        return redirect('lista_funcionarios')
    contexto={
        'form_funcionarios': form
    }    
    return render(request, 'funcionario_cadastrar.html',contexto)
def remover_funcionario(request, id):
    funcionario = funcionarios.objects.get(pk=id)
    funcionario.delete()
    return redirect('lista_funcionarios') 
@login_required    
def perfil(request):
    return render(request, 'perfil.html')            




