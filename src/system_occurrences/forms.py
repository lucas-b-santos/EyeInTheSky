from django import forms
from .models import Ocorrencia
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from datetime import datetime
import json
from core.settings import TIME_ZONE

class EnvioForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia

        fields = '__all__'

        exclude = ['user']
        
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

        
    def clean_data_hora(self):
        data_hora = self.cleaned_data.get("data_hora")

        if data_hora < datetime.now(TIME_ZONE):
            
            return data_hora
        else:
            raise ValidationError(_("Informe uma data e hora válida!"))
        
    def clean_localizacao(self):
        localizacao = self.cleaned_data.get("localizacao")

        localizacao = json.loads(localizacao)

        return localizacao



