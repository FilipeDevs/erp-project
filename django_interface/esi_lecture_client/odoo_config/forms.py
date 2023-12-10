from django import forms
from .models import OdooConfiguration


class OdooConfigForm(forms.ModelForm):
    class Meta:
        model = OdooConfiguration
        fields = '__all__'
