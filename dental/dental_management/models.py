from django.db import models
from django.utils import timezone


class Clinic(models.Model):
    """
    A Django model representing a Clinic entity.

    Attributes:
        name (CharField): The name of the clinic, with a maximum length of 255 characters.
        phone_number (CharField): The contact phone number of the clinic, with a maximum length of 20 characters.
        city (CharField): The city where the clinic is located, with a maximum length of 100 characters.
        state (CharField): The state where the clinic is located, with a maximum length of 100 characters.
        email (EmailField): The email address of the clinic, which must be unique across all Clinic instances.
    """
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Doctor(models.Model):
    """
    A model representing a doctor with various attributes.

    Attributes:
        npi (CharField): A unique National Provider Identifier for the doctor.
        name (CharField): The full name of the doctor.
        email (EmailField): A unique email address for the doctor.
        phone_number (CharField): The contact phone number for the doctor.
        specialties (CharField): A comma-separated list of the doctor's specialties.
        clinics (ManyToManyField): A many-to-many relationship with the Clinic model, representing the clinics the doctor is associated with.
    """
    npi = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    specialties = models.CharField(max_length=255)  # Comma-separated specialties
    clinics = models.ManyToManyField(Clinic)

class Patient(models.Model):
    """
    A model representing a patient in a healthcare system.

    Attributes:
        name (CharField): The full name of the patient. Maximum length is 255 characters.
        dob (DateField): The date of birth of the patient.
        phone_number (CharField): The contact phone number of the patient. Maximum length is 20 characters.
        address (TextField): The residential address of the patient.
        gender (CharField): The gender of the patient. Choices are 'Male', 'Female', or 'Other'. Maximum length is 10 characters.
        ssn_last4 (CharField): The last four digits of the patient's Social Security Number. Maximum length is 4 characters.
    """
    name = models.CharField(max_length=255)
    dob = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    ssn_last4 = models.CharField(max_length=4)

class Appointment(models.Model):
    """
    Represents an appointment in the healthcare system.

    Attributes:
        date (DateTimeField): The date and time of the appointment.
        procedure (CharField): The name or type of procedure to be performed, limited to 100 characters.
        clinic (ForeignKey): A reference to the Clinic where the appointment is scheduled.
        doctor (ForeignKey): A reference to the Doctor who will perform the procedure.
        patient (ForeignKey): A reference to the Patient who is scheduled for the appointment.
    """
    date = models.DateTimeField(default=timezone.now)
    procedure = models.CharField(max_length=100)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Visit(models.Model):
    """
    Represents a visit record in a medical context.

    Attributes:
        date (DateTimeField): The date and time of the visit.
        notes (TextField): Optional notes about the visit. Can be null or blank.
        procedures (CharField): A string of comma-separated procedures performed during the visit.
        clinic (ForeignKey): A reference to the Clinic where the visit took place. 
                            Deletes the visit if the associated Clinic is deleted.
        doctor (ForeignKey): A reference to the Doctor who attended the visit. 
                            Deletes the visit if the associated Doctor is deleted.
        patient (ForeignKey): A reference to the Patient who attended the visit. 
                            Deletes the visit if the associated Patient is deleted.
    """
    date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(null=True, blank=True)
    procedures = models.CharField(max_length=255)  # Comma-separated procedures
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
