from django import forms
from dental_management.models import Specialty

class SpecialtyForm(forms.ModelForm):
    class Meta:
        model = Specialty
        fields = ['name']
