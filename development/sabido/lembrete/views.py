from django.shortcuts import render, redirect
from .forms import LembreteForm
from .models import Lembrete
from django.http import HttpResponse
from django.views.decorators.http import require_safe, require_http_methods, require_GET, require_POST

# Create your views here.

@require_safe
def lembrete_list(request):
    context = {'lembrete_list':Lembrete.objects.all()}
    return HttpResponse(render(request, "lembrete/lembrete_list.html", context))

@require_http_methods(["GET", "POST", "PUT", "PATCH"])
def lembrete_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = LembreteForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Tarefa correspondentes à chave primária referente ao id
            lembrete = Lembrete.objects.get(pk = id)
            form = LembreteForm(instance = lembrete)
        return HttpResponse(render(request, "lembrete/lembrete_form.html", {'form': form}))
    else:
        if id == 0: # Operação de inserir uma nova Tarefa
            form = LembreteForm(request.POST)
        else: # Operação de atualizar uma Tarefa já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            lembrete = Lembrete.objects.get(pk = id)
            form = LembreteForm(request.POST, instance = lembrete)
        if form.is_valid(): 
            form.save()
        return redirect('/lembrete/list')            

def lembrete_delete(id):
    lembrete = Lembrete.objects.get(pk = id)
    lembrete.delete()
    return redirect('/lembrete/list')

