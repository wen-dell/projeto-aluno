from django import forms

from .models import Frequencia


class FrequenciaForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = ('matricula', 'faltas')
