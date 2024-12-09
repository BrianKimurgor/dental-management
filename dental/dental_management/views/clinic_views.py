from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from dental_management.models import Clinic
from dental_management.forms.clinic_forms import ClinicForm
from django.contrib.auth.decorators import login_required


# List all clinics
@login_required
def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'dental_management/clinic_list.html', {'clinics': clinics})

# View clinic details
@login_required
def clinic_detail(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    return render(request, 'dental_management/clinic_detail.html', {'clinic': clinic})

# Create a new clinic
@login_required
def clinic_create(request):
    if request.method == "POST":
        form = ClinicForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new clinic to the database
            return redirect('clinic_list')  # Redirect to the clinic list page after creation
    else:
        form = ClinicForm()  # Empty form for GET request
    return render(request, 'dental_management/clinic_form.html', {'form': form})

# Update an existing clinic
@login_required
def clinic_update(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    if request.method == "POST":
        form = ClinicForm(request.POST, instance=clinic)
        if form.is_valid():
            form.save()  # Save the updated clinic
            return redirect('clinic_detail', pk=clinic.pk)  # Redirect to the clinic detail page after update
    else:
        form = ClinicForm(instance=clinic)  # Pre-populate form with existing data
    return render(request, 'dental_management/clinic_form.html', {'form': form})

# Delete a clinic
@login_required
def clinic_delete(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    if request.method == "POST":
        clinic.delete()  # Delete the clinic from the database
        return redirect('clinic_list')  # Redirect to the clinic list after deletion
    return render(request, 'dental_management/clinic_confirm_delete.html', {'clinic': clinic})
