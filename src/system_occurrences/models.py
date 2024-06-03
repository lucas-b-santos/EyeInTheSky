from django.db import models
from accounts.models import User

class Ocorrencia(models.Model):
    '''Entidade que representa uma ocorrência de crime'''

    user = models.ForeignKey(null=True, to=User, on_delete=models.CASCADE)

    localizacao = models.JSONField()

    data_hora = models.DateTimeField(verbose_name="Data e Hora do Crime:", ) 
    
    TIPOS_CRIME = {
        'acidente_transito': "Acidente de Trânsito",
        'assalto': "Assalto",
        'homicidio': "Homicídio",
        'latrocinio': "Latrocínio",
        'outro': "Outro"
    }    
    
    tipo_crime = models.CharField(max_length=20, choices=TIPOS_CRIME, verbose_name="Tipo de Crime:")
    
    descricao = models.TextField(verbose_name="Descrição do Crime:")

    img = models.FileField(upload_to="uploads/", null=True, blank=True, verbose_name='Imagem (opcional):')
