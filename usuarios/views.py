from django.shortcuts import render
from usuarios.forms import LoginForm, CadastroForm
# Create your views here.
def login(request):
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'usuarios/login.html', context)


def cadastro(request):
    form = CadastroForm()
    context = {
        'form': form
    }
    return render(request, 'usuarios/cadastro.html', context)
