from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home',
        'content': {
            1:{
            'nome': 'Nebulosa da Carina',
            'legenda': 'webbtelescope.org/NASA/James Webb'},
            2:{
            'nome': 'Galáxia NGC 1079',
            'legenda': 'nasa.org/NASA/Hubble'},
        }
    }
    return render(request, 'home/index.html', context=context)

def image(request):
    context = {
        'title': 'Image',
    }
    return render(request, 'home/imagem.html', context=context)