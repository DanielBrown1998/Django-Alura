from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to the home',
        'images': [f'imagem{c}' for c in range(6)],
    }
    return render(request, 'home/index.html', context=context)

def image(request):
    context = {
        'title': 'Image',
        'content': 'Welcome to the image',
    }
    return render(request, 'home/imagem.html', context=context)