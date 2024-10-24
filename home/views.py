from django.shortcuts import render, get_object_or_404, redirect
from home.models import Fotografia

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
    return render(request, 'home/index.html', context=context)

def image(request, item_id):
    image = get_object_or_404(Fotografia, pk=item_id)
    context = {
        'title': f'{image.nome}',
        'item': image,
    }
    return render(request, 'home/imagem.html', context=context)

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
