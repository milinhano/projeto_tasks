from django.shortcuts import render
from .models import Tarefa

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request,'tarefas/listar_tarefas.html', {'tarefas': tarefas})

def criar_tarefa(request):
    return render(request,'tarefas/criar_tarefa.html')
