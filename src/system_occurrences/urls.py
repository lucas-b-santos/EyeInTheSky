from django.urls import path
from . import views as v

urlpatterns = [
    path("enviar_ocorrencia", v.enviar_ocorrencia, name="enviar_ocorrencia"),
]
