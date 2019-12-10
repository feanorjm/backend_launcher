from django import forms
from admin_launcher.models import *

class BackgroundForm(forms.ModelForm):
    class Meta:
        model = background
        #use_required_attribute = False
        fields = ['nombre','descripcion', 'imagen', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }
