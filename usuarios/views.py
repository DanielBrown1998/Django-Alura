from django.shortcuts import render, redirect
from usuarios.forms import LoginForm, CadastroForm
from django.contrib import auth
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib.messages import success, error

# Create your views here.
def login(request):

    if request.method == "POST":
        form = LoginForm(
            request.POST
        )
        if form.is_valid():
            user = auth.authenticate(
                request, 
                username=form["nome_login"].value(),
                password=form["senha"].value()
            )
            if user is None:
                error(request, "Usuário ou senha inválidos")
                return redirect("usuarios:login")

            auth.login(request, user)
            success(request, "Usuário logado com sucesso")
            return redirect("home:home")

    form = LoginForm()
    context = {
        'form': form,
        'bootstrap': True,
    }
    return render(request, 'usuarios/login.html', context)


def cadastro(request):

    if request.method == "POST":
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            nome = form['nome'].value()
            email = form['email'].value()
            senha = form['senha'].value()
            
            if User.objects.filter(username=nome).exists():
                error(request, "Usuário já cadastrado")
                return redirect("usuarios:cadastro")

            usuario = User.objects.create_user(
                username=nome, 
                email=email,
                password=senha
            )
            usuario.save()
            success(request, "Cadastro criado com sucesso")
            return redirect("usuarios:login")
        else:
            for _, errors_field in form.errors.as_data().items():
                for error_field in errors_field:
                    error(request, f"{error_field.message}")
            return redirect("usuarios:cadastro")

    form = CadastroForm()
    context = {
        'form': form,
        'bootstrap': True,
    }
    return render(request, 'usuarios/cadastro.html', context)

@login_required(login_url='usuarios:login')
def logout(request):
    user = get_user(request)
    auth.logout(request)
    success(request, f'{user.username} saiu!')
    return redirect('usuarios:login')