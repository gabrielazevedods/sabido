from django.shortcuts import render, redirect
from .forms import ProjetoForm
from .models import Projeto
from django.http import HttpResponse
from django.views.decorators.http import require_safe, require_http_methods

# Create your views here.

@require_http_methods(["GET", "POST"])
def projeto_list(request):
    context = {'projeto_list':Projeto.objects.all()}
    return HttpResponse(render(request, "projeto/projeto_list.html", context))

@require_http_methods(["GET", "POST"])
def projeto_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = ProjetoForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados das projetos correspondentes à chave primária referente ao id
            projeto = Projeto.objects.get(pk = id)
            form = ProjetoForm(instance = projeto)
        return HttpResponse(render(request, "projeto/projeto_form.html", {'form': form}))
    else:
        if id == 0: # Operação de inserir um novo projeto
            form = ProjetoForm(request.POST)
        else: # Operação de atualizar uma projeto já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            projeto = Projeto.objects.get(pk = id)
            form = ProjetoForm(request.POST, instance = projeto)
        if form.is_valid(): 
            form.save()
        return redirect('/projeto/list')          

@require_http_methods(["GET", "POST"])
def projeto_delete(id):
    projeto = Projeto.objects.get(pk = id)
    projeto.delete()
    return redirect('/projeto/list')

