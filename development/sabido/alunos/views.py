from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno

# Create your views here.

def alunos_list(request):
    context = {'alunos_list':Aluno.objects.all()}
    return render(request, "aluno/alunos_list.html", context)

def alunos_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = AlunoForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Compromisso correspondentes à chave primária referente ao id
            alunos = Aluno.objects.get(pk = id)
            form = AlunoForm(instance = alunos)
        return render(request, "aluno/alunos_form.html", {'form': form})
    else:
        if id == 0: # Operação de inserir um novo Compromisso
            form = AlunoForm(request.POST)
        else: # Operação de atualizar um Compromisso já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            alunos = Aluno.objects.get(pk = id)
            form = AlunoForm(request.POST, instance = alunos)
        if form.is_valid(): 
            form.save()
        return redirect('/alunos/list')            

def alunos_delete(request, id):
    alunos = Aluno.objects.get(pk = id)
    alunos.delete()
    return redirect('/alunos/list')

