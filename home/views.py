from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'title': 'Home',
        'content': 'Welcome to the home',
    }
    return render(request, 'home/index.html', context=context)
