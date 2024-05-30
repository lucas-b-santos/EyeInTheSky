from .forms import EnvioForm

class EnvioCrimeController(EnvioForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
