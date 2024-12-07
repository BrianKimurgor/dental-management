from django.db import models

class Patient(models.Model):
    """
    Represents a patient in the healthcare system.
    """
    name = models.CharField(max_length=255)
    dob = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    ssn_last4 = models.CharField(max_length=4)

    def __str__(self):
        return self.name
