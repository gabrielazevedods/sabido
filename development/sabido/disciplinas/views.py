from django.shortcuts import render, redirect
from .forms import DisciplinaForm
from .models import Disciplina

# Create your views here.

def disciplinas_list(request):
    context = {'disciplinas_list':Disciplina.objects.all()}
    return render(request, "disciplinas/disciplinas_list.html", context)

def disciplinas_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = DisciplinaForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Compromisso correspondentes à chave primária referente ao id
            disciplinas = Disciplina.objects.get(pk = id)
            form = DisciplinaForm(instance = disciplinas)
        return render(request, "disciplinas/disciplinas_form.html", {'form': form})
    else:
        if id == 0: # Operação de inserir um novo Compromisso
            form = DisciplinaForm(request.POST)
        else: # Operação de atualizar um Compromisso já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            disciplinas = Disciplina.objects.get(pk = id)
            form = DisciplinaForm(request.POST, instance = disciplinas)
        if form.is_valid(): 
            form.save()
        return redirect('/disciplinas/list')            

def disciplinas_delete(request, id):
    disciplinas = Disciplina.objects.get(pk = id)
    disciplinas.delete()
    return redirect('/disciplinas/list')

