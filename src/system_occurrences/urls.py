from django.urls import path
from . import views as v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("enviar_ocorrencia", v.enviar_ocorrencia, name="enviar_ocorrencia"),
    path("visualizar", v.ver_ocorrencias, name="ver_ocorrencias"),
] 
