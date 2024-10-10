from django.db import models

# Create your models here.

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return f"fotografia: [nome={self.nome}]"


nome='Nebulosa da Carina'
legenda='webbtelescope.org/NASA/James Webb'
descricao='A nebulosa da Carina é uma nuvem de poeira e gases que se localiza na constelação de Carina, a cerca de 6.500 anos-luz da Terra. A nebulosa é uma região de formação estelar, onde o gás e a poeira se condensam para formar estrelas. A nebulosa é conhecida por suas formas complexas e coloridas, que são criadas pela radiação das estrelas jovens que se formam dentro dela.'
foto='carina-nebula.png'
