from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to the home',
    }
    return render(request, 'home/index.html', context=context)
