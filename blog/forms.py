from django import forms
from .models import RegistroRescatados

class PostForm(forms.ModelForm):

        class Meta:
            model = RegistroRescatados
            fields = ('Nombre', 'Fotografia','RazaPredominante','Descripcion','Estado')
