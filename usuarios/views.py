from django.shortcuts import render, redirect

def login(request):
    if request.method == 'POST':
        return redirect('listar_tarefas')  # por enquanto, sem validar nada
    return render(request, 'usuarios/login.html')
    
