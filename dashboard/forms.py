from django import forms
from .models import Bond

class BondForm(forms.ModelForm):
    class Meta:
        model = Bond
        fields = ['description']