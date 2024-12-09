from rest_framework import serializers
from dental_management.models.patient import Patient

class PatientSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(format='%Y-%m-%d', input_formats=['%Y-%m-%d'])
    class Meta:
        model = Patient
        fields = '__all__'
