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
from core.views import home, adiministrador,lista_percas, lista_percas, moto, progresso, percas_cadastrar,editar_percas,remover_percas

urlpatterns = [
    path('', home),
    path('adiministrador/',adiministrador,name='adiministrador'),
    path('moto/',moto,name='moto'),
    path('progresso/',progresso,name='progresso'),
    path('percas_cadastrar/', percas_cadastrar, name='percas_cadastrar'),
    path('lista_percas/', lista_percas, name='lista_percas'),
    path('percas_editar/<int:id>/', editar_percas, name='editar_percas'),
    path('percas_remover/<int:id>/', remover_percas, name='remover_percas'),
    path('admin/', admin.site.urls),
]
