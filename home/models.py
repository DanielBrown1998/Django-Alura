from django.db import models

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
    foto = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return f"fotografia: [nome={self.nome}]"
