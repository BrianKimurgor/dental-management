from django.db import models
from .doctor import Doctor
from .clinic import Clinic
from .patient import Patient

class Appointment(models.Model):
    """
    Represents an appointment in the system.
    """
    date_time = models.DateTimeField()  # Date and time of the appointment
    procedure = models.CharField(max_length=100)  # Procedure name
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')

    def __str__(self):
        return f"{self.procedure} for {self.patient.name} with Dr. {self.doctor.name} on {self.date_time}"
