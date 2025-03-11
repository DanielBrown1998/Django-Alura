from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from apps.home.models import Fotografia
from apps.home.forms import FotografiaForm
from django.contrib.messages import success, error

@login_required(login_url='usuarios:login')
def home(request):

    fotografias = Fotografia.objects.filter(
        publicada=True
    ).order_by(
        "data_fotografia"
    )

    context = {
        'title': 'Home',
        'content': fotografias,
    }
    return render(request, 'index.html', context=context)

@login_required(login_url='usuarios:login')
def image(request, id:int):
    image = get_object_or_404(Fotografia, pk=id)
    context = {
        'title': f'{image.nome}',
        'item': image,
        "item_id": id
    }
    return render(request, 'home/imagem.html', context=context)

@login_required(login_url='usuarios:login')
def tag(request, categoria):
    
    TAG = Fotografia.objects.filter(
        categoria__icontains = categoria
    )

    print(TAG)
    context = {
        'title': f'Tag:{categoria}',
        'content': TAG,
    }

    return render(
        request, 'home/index.html', context=context
    )

@login_required(login_url='usuarios:login')
def buscar(request):
    if 'buscar' in request.GET:
        info = str(request.GET.get('buscar')).strip()
        if info:
            resultado = Fotografia.objects.filter(nome__icontains=info)
        else:
            resultado = Fotografia.objects.all()
    context ={
        'title': 'Buscar',
        'content': resultado, 
    }

    return render(request, 'home/buscar.html', context=context)


@login_required(login_url='usuarios:login')
def nova_imagem(request):

    if request.method == 'POST':
        forms = FotografiaForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            msg = 'Imagem salva com sucesso!'
            success(request, msg)
            return render(request, 'index.html')
        else:
            error(request, 'Erro ao salvar a imagem!')
            return render(request, 'home/nova_imagem.html', {'form': forms})
    forms = FotografiaForm
    context = {
        'title': 'Nova Imagem',
        'form': forms
    }
    return render(request, 'home/nova_imagem.html', context=context)

@login_required(login_url='usuarios:login')
def editar_imagem(request, id:int):

    fotografia = Fotografia.objects.get(pk=id) 
    forms = FotografiaForm(instance=fotografia)

    context = {
        'title': 'Editar Imagem',
        'form': forms,
        'foto_id': id
    }

    if request.method == "POST":
        forms = FotografiaForm(request.POST, request.FILES, instance=Fotografia)
        if forms.is_valid():
            forms.save()
            msg = 'Imagem editada com sucesso!'
            success(request, msg)
            return render(request, 'index.html')
        else:
            error(request, 'Erro ao editar a imagem!')
            return render(request, 'home/editar_imagem.html', context)
    
    return render(request, 'home/editar_imagem.html', context)

@login_required(login_url='usuarios:login')
def deletar_imagem(request, id:int):
    return redirect("home:home")
