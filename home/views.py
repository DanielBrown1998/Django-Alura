from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to the home',
    }
    return render(request, 'home/index.html', context=context)

def image(request):
    context = {
        'title': 'Image',
        'content': 'Welcome to the image',
    }
    return render(request, 'home/imagem.html', context=context)