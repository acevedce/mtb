from django import forms

from .models import molecule

class PostForm(forms.ModelForm):

    class Meta:
        model = molecule
        fields = ('ChemblID',)