from django.contrib import admin
from home.models import Fotografia
# Register your models here.


#admin.site.register(Fotografia)
@admin.register(Fotografia)
class FotografiaAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 
        'legenda',
        'categoria', 
        'descricao', 
        'foto',
        ]
    search_fields = [
        'nome',
        'categoria',
        'foto',
        ]
    list_filter = ["categoria", ]
    list_per_page = 10
    ordering = ['nome',]
