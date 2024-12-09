from django import forms
from dental_management.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date_time', 'procedure', 'clinic', 'doctor', 'patient']
        
    # Optionally pre-populate the patient field in the form (if relevant)
    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)  # Extract user from kwargs
    #     super().__init__(*args, **kwargs)

    #     # Example usage of self.user
    #     if self.user and self.user.is_authenticated:
    #         self.fields['doctor'].queryset = self.user.doctors.all()  # Customize based on user