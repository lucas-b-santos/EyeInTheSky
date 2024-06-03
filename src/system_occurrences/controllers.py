from .forms import EnvioForm
from accounts.models import User

class EnvioCrimeController(EnvioForm):
    '''Controlador de Envio de Ocorrências de Crimes'''
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
    
        self._envioAnonimo = self.data.get('envio-anonimo')


    def saveOccurrence(self, user_id):
        '''Salva ocorrência, associando usuário caso não foi optado por envio anônimo'''
        
        if self._envioAnonimo:
            self.save()
            
        else:
            occurrence = self.save(commit=False)
            
            occurrence.user = User.objects.get(id=user_id)
            
            occurrence.save()