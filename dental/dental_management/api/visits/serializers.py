from rest_framework import serializers
from dental_management.models.visit import Visit

class VisistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
