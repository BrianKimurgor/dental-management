from django.db import models

class Specialty(models.Model):
    """
    Represents a medical specialty.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
