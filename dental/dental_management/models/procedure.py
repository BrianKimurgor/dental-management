from django.db import models

class Procedure(models.Model):
    """
    Represents a medical procedure.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
