from django import forms
from .models import Ocorrencia
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from datetime import datetime
from core.settings import TIME_ZONE
from pytz import timezone
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
            if field_name == 'localizacao':
                field.widget.attrs["class"] += " d-none"
                
            if field_name == 'descricao':
                field.widget.attrs["rows"] = 3

    def clean_data_hora(self):
        data_hora = self.cleaned_data.get("data_hora")

        if data_hora < datetime.now(timezone(TIME_ZONE)):
            
            return data_hora
        
        else:
            
            raise ValidationError(_("Informe uma data e hora válida!"))
        



