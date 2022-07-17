from django.shortcuts import render, redirect
from .forms import KanbanToDoForm 
from .forms import KanbanDoingForm 
from .forms import KanbanDoneForm 
from .models import KanbanToDo
from .models import KanbanDoing
from .models import KanbanDone
from django.http import HttpResponse
from django.views.decorators.http import require_safe, require_http_methods

KANBAN_LIST = '/kanban/list'

# Create your views here.

@require_http_methods(["GET", "POST"])
def kanban_list(request):
    context = {'kanban_todo_list':KanbanToDo.objects.all(), 'kanban_doing_list':KanbanDoing.objects.all(), 'kanban_done_list':KanbanDone.objects.all()}
    return HttpResponse(render(request, "kanban/kanban_list.html", context))

@require_http_methods(["GET", "POST"])
def kanban_todo_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = KanbanToDoForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Kanban correspondentes à chave primária referente ao id
            kanbantodo = KanbanToDo.objects.get(pk = id)
            form = KanbanToDoForm(instance = kanbantodo)
        return HttpResponse(render(request, "kanban/kanban_todo_form.html", {'form': form}))
    else:
        if id == 0: # Operação de inserir uma tarefa em uma divisão do Kanban
            form = KanbanToDoForm(request.POST)
        else: # Operação de atualizar um Kanban já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            kanbantodo = KanbanToDo.objects.get(pk = id)
            form = KanbanToDoForm(request.POST, instance = kanbantodo)
        if form.is_valid(): 
            form.save()
        return redirect(KANBAN_LIST)    

@require_http_methods(["GET", "POST"])
def kanban_doing_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = KanbanDoingForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Kanban correspondentes à chave primária referente ao id
            kanbandoing = KanbanDoing.objects.get(pk = id)
            form = KanbanDoingForm(instance = kanbandoing)
        return HttpResponse(render(request, "kanban/kanban_doing_form.html", {'form': form}))
    else:
        if id == 0: # Operação de inserir uma tarefa em uma divisão do Kanban
            form = KanbanDoingForm(request.POST)
        else: # Operação de atualizar um Kanban já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            kanbandoing = KanbanDoing.objects.get(pk = id)
            form = KanbanDoingForm(request.POST, instance = kanbandoing)
        if form.is_valid(): 
            form.save()
        return redirect(KANBAN_LIST)

@require_http_methods(["GET", "POST"])
def kanban_done_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = KanbanDoneForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Kanban correspondentes à chave primária referente ao id
            kanbandone = KanbanDone.objects.get(pk = id)
            form = KanbanDoneForm(instance = kanbandone)
        return HttpResponse(render(request, "kanban/kanban_done_form.html", {'form': form}))
    else:
        if id == 0: # Operação de inserir uma tarefa em uma divisão do Kanban
            form = KanbanDoneForm(request.POST)
        else: # Operação de atualizar um Kanban já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            kanbandone = KanbanDone.objects.get(pk = id)
            form = KanbanDoneForm(request.POST, instance = kanbandone)
        if form.is_valid(): 
            form.save()
        return redirect(KANBAN_LIST)        

@require_http_methods(["GET", "POST"])
def kanban_todo_delete(id):
    kanbantodo = KanbanToDo.objects.get(pk = id)
    kanbantodo.delete()
    return redirect(KANBAN_LIST)

@require_http_methods(["GET", "POST"])
def kanban_doing_delete(id):
    kanbandoing = KanbanDoing.objects.get(pk = id)
    kanbandoing.delete()
    return redirect(KANBAN_LIST)

@require_http_methods(["GET", "POST"])
def kanban_done_delete(id):
    kanbandone = KanbanDone.objects.get(pk = id)
    kanbandone.delete()
    return redirect(KANBAN_LIST)

