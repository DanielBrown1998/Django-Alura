from django.contrib import admin
from home.models import Fotografia
# Register your models here.


#admin.site.register(Fotografia, FotografiaAdmin)
@admin.register(Fotografia)
class FotografiaAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 
        'categoria',
        'publicada', 
        ]
    search_fields = [
        'nome',
        'categoria',
        'foto',
        ]
    
    list_editable = ["publicada",]

    list_filter = ["categoria","usuario",]
    list_per_page = 10
    ordering = ['nome',]
