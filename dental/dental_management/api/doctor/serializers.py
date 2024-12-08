from rest_framework import serializers
from dental_management.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'phone_number', 'specialties']
