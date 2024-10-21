from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from django.contrib.auth import login, logout  # type: ignore
from django.contrib import messages  # type: ignore
from tarefas.models import CadastroTarefas, Usuario
from .forms import CadastroTarefasForm, AtualizarTarefasForm, CPFLoginForm, UsuarioForm, TarefaForm
from django.contrib.auth.decorators import login_required  # type: ignore
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import check_password

@login_required
def lista_tarefas(request):
    tarefas = CadastroTarefas.objects.filter(responsavel=request.user)
    return render(request, 'tarefas/home.html', {'cadastro_tarefas': tarefas})

def adicionar_tarefa(request):
    if request.method == 'POST':
        form = CadastroTarefasForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa adicionada com sucesso!')
            return redirect('lista_tarefas')
    else:
        form = CadastroTarefasForm(user=request.user)

    return render(request, 'forms/adicionar_tarefa.html', {'form': form})

def detalhe_tarefa(request, tarefa_id):
    cadastro_tarefa = get_object_or_404(CadastroTarefas, id=tarefa_id)

    if request.method == 'POST':
        form = AtualizarTarefasForm(request.POST, instance=cadastro_tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('lista_tarefas')  # Redireciona para a lista de tarefas do usuário
    else:
        form = AtualizarTarefasForm(instance=cadastro_tarefa)

    return render(request, 'tarefas/detalhe.html', {
        'cadastro_tarefa': cadastro_tarefa,
        'form': form
    })


def login_view(request):
    if request.method == 'POST':
        form = CPFLoginForm(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            senha = form.cleaned_data['senha']

            user = Usuario.objects.filter(cpf=cpf).first()

            if user and check_password(senha, user.password):
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('lista_tarefas')
            else:
                form.add_error(None, "CPF ou senha incorretos.")
    else:
        form = CPFLoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def excluir_tarefa(request, tarefa_id):
    cadastro_tarefa = get_object_or_404(CadastroTarefas, id=tarefa_id)
    cadastro_tarefa.delete()
    messages.success(request, 'Tarefa excluída com sucesso!')
    return redirect('lista_tarefas')

@user_passes_test(lambda u: u.is_superuser)
def add_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = UsuarioForm()
    
    return render(request, 'add.html', {'form': form})

def add_tarefa_view(request):
    if request.method == 'POST':
        form = CadastroTarefasForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = CadastroTarefasForm(user=request.user)

    return render(request, 'addtarefa.html', {'form': form}) 

@user_passes_test(lambda u: u.is_superuser)
def detalhes_usuarios(request):
    if not request.user.is_superuser:
        return redirect('lista_tarefas')

    usuarios = Usuario.objects.all()
    tarefas = CadastroTarefas.objects.all()

    return render(request, 'detalhesusuarios.html', {'usuarios': usuarios, 'tarefas': tarefas})

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    tarefas = CadastroTarefas.objects.filter(responsavel=usuario)

    if request.method == 'POST':
        usuario_form = UsuarioForm(request.POST, instance=usuario)
        if usuario_form.is_valid():
            usuario_form.save()

            # Para cada tarefa, verificar se existe um form correspondente no POST
            for tarefa in tarefas:
                tarefa_form = CadastroTarefasForm(request.POST, instance=tarefa)
                if tarefa_form.is_valid():
                    tarefa_form.save()
            messages.success(request, 'Usuário e tarefas atualizados com sucesso!')
            return redirect('detalhes_usuarios')  # Redireciona para a página de detalhes dos usuários
    else:
        usuario_form = UsuarioForm(instance=usuario)
        tarefa_forms = [CadastroTarefasForm(instance=tarefa) for tarefa in tarefas]

    return render(request, 'editar_usuario.html', {
        'usuario_form': usuario_form,
        'tarefa_forms': tarefa_forms,
        'usuario': usuario,
    })


@user_passes_test(lambda u: u.is_superuser)
def deletar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        usuario.delete()
        return redirect('detalhes_usuarios')
    
    return render(request, 'confirmar_deletar_usuario.html', {'usuario': usuario})


def detalhe_tarefa(request, tarefa_id):
    cadastro_tarefa = get_object_or_404(CadastroTarefas, id=tarefa_id)

    if request.method == 'POST':
        form = AtualizarTarefasForm(request.POST, instance=cadastro_tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('lista_tarefas')  # Redireciona para a lista de tarefas do usuário
    else:
        form = AtualizarTarefasForm(instance=cadastro_tarefa)

    return render(request, 'tarefas/detalhe.html', {
        'cadastro_tarefa': cadastro_tarefa,
        'form': form
    })
