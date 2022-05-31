from django.shortcuts import render, redirect
from .forms import CursosForm
from .models import Cursos

# Create your views here.

def Cursos_list(request):
    context = {'cursos_list':Cursos.objects.all()}
    return render(request, "cursos/cursos_list.html", context)

def Cursos_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = CursosForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Tarefa correspondentes à chave primária referente ao id
            cursos = Cursos.objects.get(pk = id)
            form = CursosForm(instance = cursos)
        return render(request, "cursos/cursos_form.html", {'form': form})
    else:
        if id == 0: # Operação de inserir uma nova Tarefa
            form = CursosForm(request.POST)
        else: # Operação de atualizar uma Tarefa já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            cursos = Cursos.objects.get(pk = id)
            form = CursosForm(request.POST, instance = cursos)
        if form.is_valid(): 
            form.save()
        return redirect('/cursos/list')            

def Cursos_delete(request, id):
    cursos = Cursos.objects.get(pk = id)
    cursos.delete()
    return redirect('/cursos/list')
