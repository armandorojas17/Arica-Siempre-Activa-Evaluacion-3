from django import forms
from .models import Actividad


class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = [
            'titulo',
            'categoria',
            'fecha',
            'descripcion',
            'precio',
            'cupo_maximo',
            'imagen'
        ]

