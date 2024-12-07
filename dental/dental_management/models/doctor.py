from django.db import models
from .clinic import Clinic
from .specialty import Specialty

class Doctor(models.Model):
    """
    Represents a doctor with normalized specialties.
    """
    npi = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    specialties = models.ManyToManyField(Specialty)
    clinics = models.ManyToManyField(Clinic)

    def __str__(self):
        return self.name
