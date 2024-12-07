from django.db import models
from django.utils import timezone
from .clinic import Clinic
from .doctor import Doctor
from .patient import Patient
from .procedure import Procedure

class Visit(models.Model):
    """
    Represents a visit record with normalized procedures.
    """
    date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(null=True, blank=True)
    procedures = models.ManyToManyField(Procedure)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"Visit on {self.date} by {self.doctor.name}"
