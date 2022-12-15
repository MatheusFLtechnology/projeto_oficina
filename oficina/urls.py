"""oficina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from core.views import editar_funcionario, home, adiministrador,lista_percas, lista_percas, moto, progresso, percas_cadastrar,editar_percas, remover_funcionario,remover_percas, adimin,lista_funcionarios,cadastrar_funcionario, editar_funcionario, remover_funcionario,perfil

urlpatterns = [
    path('', home, name='home'),
    path('adiministrador/',adiministrador,name='adiministrador'),
    path('adimin/',adimin,name='admin'),
    path('moto/',moto,name='moto'),
    path('progresso/',progresso,name='progresso'),
    path('percas_cadastrar/', percas_cadastrar, name='percas_cadastrar'),
    path('lista_percas/', lista_percas, name='lista_percas'),
    path('percas_editar/<int:id>/', editar_percas, name='editar_percas'),
    path('lista_funcionarios/',lista_funcionarios,name='lista_funcionarios'),
    path('funcionario_cadastrar/',cadastrar_funcionario,name='cadastrar_funcionario'),
    path('percas_remover/<int:id>/', remover_percas, name='remover_percas'),
    path('funcionario_editar/<int:id>/', editar_funcionario, name='editar_funcionario'),
    path('funcionario_remover/<int:id>/', remover_funcionario, name='remover_funcionario'),
    path('perfil/', perfil, name='perfil'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('admin/', admin.site.urls),
]
