from system_occurrences.models import Ocorrencia
from core.settings import TIME_ZONE
from pytz import timezone

def run():
    for ocorrencia in Ocorrencia.objects.all():
        print("=============================")
        
        if ocorrencia.user:
            print("Usuário: ", ocorrencia.user.username)
        else:
            print("Anônimo")

        print(ocorrencia.data_hora.astimezone(timezone(TIME_ZONE)))
        print(ocorrencia.tipo_crime)
        print(ocorrencia.localizacao)
        
        if ocorrencia.img:
            print(ocorrencia.img.url)
        print("=============================")
