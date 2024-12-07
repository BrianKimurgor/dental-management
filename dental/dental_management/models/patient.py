from django.db import models

class Patient(models.Model):
    """
    A model representing a patient in the healthcare system.

    Attributes:
        name (CharField): The full name of the patient. Maximum length is 255 characters.
        dob (DateField): The date of birth of the patient.
        phone_number (CharField): The contact phone number of the patient. Maximum length is 20 characters.
        address (TextField): The residential address of the patient.
        gender (CharField): The gender of the patient. Choices are 'Male', 'Female', or 'Other'. Maximum length is 10 characters.
        ssn_last4 (CharField): The last four digits of the patient's Social Security Number. Maximum length is 4 characters.
    """
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    dob = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    ssn_last4 = models.CharField(max_length=4)

    def __str__(self):
        return self.name
