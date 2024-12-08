from django import forms
from dental_management.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date_time', 'procedure', 'clinic', 'doctor', 'patient']
        
    # Optionally pre-populate the patient field in the form (if relevant)
    def __init__(self, *args, **kwargs):
        user = kwargs.get('user')  # Get user from view
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if user.is_authenticated:
            self.fields['patient'].queryset = user.patients.all()  # Assuming `patients` is related to user
