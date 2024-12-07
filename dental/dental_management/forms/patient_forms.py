from django import forms
from dental_management.models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'dob', 'phone_number', 'address', 'gender', 'ssn_last4']
