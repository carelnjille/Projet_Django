from django import forms
from .models import Quartier, Maison

class QuartierForm(forms.ModelForm):
    class Meta:
        model = Quartier
        fields = ['nom', 'superficie']

class MaisonForm(forms.ModelForm):
    class Meta:
        model = Maison
        fields = ['quartier', 'nom', 'superficie', 'nb_chambres', 'nb_douches']
