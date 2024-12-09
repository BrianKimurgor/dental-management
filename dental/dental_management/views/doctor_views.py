from django.shortcuts import render, get_object_or_404, redirect
from dental_management.models import Doctor
from dental_management.forms.doctor_forms import DoctorForm
from django.contrib.auth.decorators import login_required

# List all doctors
@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'dental_management/doctor_list.html', {'doctors': doctors})

# View doctor details
@login_required
def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'dental_management/doctor_detail.html', {'doctor': doctor})

# Create a new doctor
@login_required
def doctor_create(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')  # Redirect to the doctor list page after creating
    else:
        form = DoctorForm()
    return render(request, 'dental_management/doctor_form.html', {'form': form})

# Update an existing doctor
@login_required
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_detail', pk=doctor.pk)
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'dental_management/doctor_form.html', {'form': form})

# Delete a doctor
@login_required
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == "POST":
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'dental_management/doctor_confirm_delete.html', {'doctor': doctor})
