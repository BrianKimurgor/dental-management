from django.db import models
from django.utils import timezone
from .clinic import Clinic
from .doctor import Doctor
from .patient import Patient
from .procedure import Procedure

class Appointment(models.Model):
    """
    Represents an appointment in the healthcare system.
    """
    date = models.DateTimeField(default=timezone.now)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.procedure.name} on {self.date}"
