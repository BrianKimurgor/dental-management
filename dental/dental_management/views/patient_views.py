from django.shortcuts import render, get_object_or_404, redirect
from dental_management.models import Patient
from dental_management.forms.patient_forms import PatientForm

# List all patients
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'dental_management/patient_list.html', {'patients': patients})

# View patient details
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'dental_management/patient_detail.html', {'patient': patient})

# Create a new patient
def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'dental_management/patient_form.html', {'form': form})

# Update an existing patient
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'dental_management/patient_form.html', {'form': form})

# Delete a patient
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient.delete()
        return redirect('patient_list')
    return render(request, 'dental_management/patient_confirm_delete.html', {'patient': patient})
