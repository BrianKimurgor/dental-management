from rest_framework import viewsets
from dental_management.models.visit import Visit
from .serializers import VisistSerializer

class VisitViewSet(viewsets.ModelViewSet):
    
    queryset = Visit.objects.all()
    serializer_class = VisistSerializer
