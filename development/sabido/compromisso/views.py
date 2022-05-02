from django.shortcuts import render, redirect
from .forms import CompromissoForm
from .models import Compromisso

# Create your views here.

def compromisso_list(request):
    context = {'compromisso_list':Compromisso.objects.all()}
    return render(request, "compromisso/compromisso_list.html", context)

def compromisso_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = CompromissoForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Compromisso correspondentes à chave primária referente ao id
            compromisso = Compromisso.objects.get(pk = id)
            form = CompromissoForm(instance = compromisso)
        return render(request, "compromisso/compromisso_form.html", {'form': form})
    else:
        if id == 0: # Operação de inserir um novo Compromisso
            form = CompromissoForm(request.POST)
        else: # Operação de atualizar um Compromisso já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            compromisso = Compromisso.objects.get(pk = id)
            form = CompromissoForm(request.POST, instance = compromisso)
        if form.is_valid(): 
            form.save()
        return redirect('/compromisso/list')            

def compromisso_delete(request, id):
    compromisso = Compromisso.objects.get(pk = id)
    compromisso.delete()
    return redirect('/compromisso/list')

