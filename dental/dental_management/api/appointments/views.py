from rest_framework import viewsets
from dental_management.models.appointment import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    
    queryset =Appointment.objects.all()
    serializer_class = AppointmentSerializer
