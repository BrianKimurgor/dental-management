from django import forms
from dental_management.models import Visit

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['notes', 'procedures', 'clinic', 'doctor', 'patient']
