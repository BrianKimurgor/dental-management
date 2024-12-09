from rest_framework import serializers
from dental_management.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'email', 'phone_number', 'npi', 'specialties']
        extra_kwargs = {
            'npi': {'required': True, 'allow_blank': False},  # Ensure NPI is required and not blank
        }

    def validate_npi(self, value):
        if Doctor.objects.filter(npi=value).exists():
            raise serializers.ValidationError("A doctor with this NPI already exists.")
        return value
