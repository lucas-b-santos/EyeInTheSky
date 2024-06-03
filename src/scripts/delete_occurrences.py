from system_occurrences.models import Ocorrencia

def run():
    for ocorrencia in Ocorrencia.objects.all():
        ocorrencia.delete()
