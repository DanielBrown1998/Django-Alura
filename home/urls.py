


from django.urls import path
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('imagem/<int:item_id>/', views.image, name='imagem'),
    path('tag/<str:categoria>/', views.tag, name='tag'),
    path('buscar/', views.buscar, name='buscar'),
]
