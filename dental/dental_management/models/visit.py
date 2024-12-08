from django.db import models
from .doctor import Doctor
from .clinic import Clinic
from .patient import Patient

class Visit(models.Model):
    """
    Represents a patient's visit record.
    """
    date_time = models.DateTimeField(auto_now_add=True)  # Automatically record visit time
    notes = models.TextField(null=True, blank=True)  # Optional notes about the visit
    procedures = models.CharField(max_length=255)  # Comma-separated procedures
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='visits')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='visits')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')

    def __str__(self):
        return f"Visit by {self.patient.name} at {self.clinic.name} with Dr. {self.doctor.name}"
