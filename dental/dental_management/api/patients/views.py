from rest_framework import viewsets
from dental_management.models.patient import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
