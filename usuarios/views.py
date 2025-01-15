from django.shortcuts import render, redirect
from usuarios.forms import LoginForm, CadastroForm
from django.contrib import auth
from django.contrib.auth.models import User 

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
            auth.login(request, user)
            print("usuário logado")
            return redirect("home:home")

    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'usuarios/login.html', context)


def cadastro(request):

    if request.method == "POST":
        form = CadastroForm(request.POST)
        
        if form.is_valid():
            if form['senha'].value() != form['confirmar_senha'].value():
                print("senha inválida")
                return redirect("usuarios:cadastro")

            nome = form['nome'].value()
            email = form['email'].value()
            senha = form['senha'].value()
            
            if User.objects.filter(username=nome).exists():
                print("já existe um usuário com esse username")
                return redirect("usuarios:cadastro")

            usuario = User.objects.create_user(
                username=nome, 
                email=email,
                password=senha
            )
            usuario.save()
            print("cadastro criado com sucesso")
            return redirect("usuarios:login")

    form = CadastroForm()
    context = {
        'form': form
    }
    return render(request, 'usuarios/cadastro.html', context)
