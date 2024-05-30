from django.db import models
from accounts.models import User

# Create your models here.

class Ocorrencia(models.Model):

    user = models.ForeignKey(null=True, to=User, on_delete=models.CASCADE)

    localizacao = models.JSONField()

    data_hora = models.DateTimeField(verbose_name="Data e Hora do crime:", ) 
    
    TIPOS_CRIME = {
        'acidente_transito': "Acidente de Trânsito",
        'assalto': "Assalto",
        'homicidio': "Homicídio",
        'latrocinio': "Latrocínio",
        'outro': "Outro"
    }    
    
    tipo_crime = models.CharField(max_length=20, choices=TIPOS_CRIME, verbose_name="Tipo de Crime:")
    
    descricao = models.TextField(verbose_name="Descrição do crime:")

    img = models.FileField(upload_to="uploads/", null=True, verbose_name='Imagem (opcional):')
