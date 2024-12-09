from rest_framework import viewsets
from dental_management.models.clinic import Clinic
from .serializers import ClinicSerializer

class ClinicViewSet(viewsets.ModelViewSet):
    
    queryset =Clinic.objects.all()
    serializer_class = ClinicSerializer
