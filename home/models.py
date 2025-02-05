import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Fotografia(models.Model):
    OPCOES = [
        ("NEBULOSA", "Nebulosa"),
        ("GALAXIA", "Galaxia"),
        ("PLANETA", "Planeta"),
        ("ESTRELA", "Estrela"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(
        max_length=150, choices=OPCOES, default=""
        )
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(
        upload_to=f"fotos/%Y/%m/%d/"
    )
    publicada = models.BooleanField(
        default=False, null=False, blank=False
    )
    data_fotografia = models.DateTimeField(
        default= datetime.datetime.now, null=True, blank=True)
    usuario = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        null=True,
        blank=False,
        related_name='user',
    )


    def __str__(self):
        return self.nome
