from django.shortcuts import render, get_object_or_404
from dental_management.models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'dental_management/patient_list.html', {'patients': patients})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'dental_management/patient_detail.html', {'patient': patient})
