


from django.urls import path
from apps.home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('imagem/<int:item_id>/', views.image, name='imagem'),
    path('tag/<str:categoria>/', views.tag, name='tag'),
    path('buscar/', views.buscar, name='buscar'),
    path('nova-imagem/', views.nova_imagem, name='nova-imagem'),
    path('editar-imagem/<int:item_id>/', views.editar_imagem, name='editar-imagem'),
    path('deletar-imagem/<int:item_id>/', views.deletar_imagem, name='deletar-imagem'),
]
