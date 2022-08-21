from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import percasForm
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
    percas = percas.object.all()
    contexto ={
        'todas_percas': percas
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