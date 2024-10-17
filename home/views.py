from django.shortcuts import render, get_object_or_404
from home.models import Fotografia

def home(request):

    fotografias = Fotografia.objects.all()

    context = {
        'title': 'Home',
        'content': fotografias,
    }
    return render(request, 'home/index.html', context=context)

def image(request, item_id):
    image = get_object_or_404(Fotografia, pk=item_id)
    context = {
        'title': 'Image',
        'item': image,
    }
    return render(request, 'home/imagem.html', context=context)