from django.shortcuts import render, get_object_or_404, redirect
from dental_management.models import Specialty
from dental_management.forms.specialty_form import SpecialtyForm

# List all specialties
def specialty_list(request):
    specialties = Specialty.objects.all()
    return render(request, 'dental_management/specialty_list.html', {'specialties': specialties})

# View specialty details
def specialty_detail(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)
    return render(request, 'dental_management/specialty_detail.html', {'specialty': specialty})

# Create a new specialty
def specialty_create(request):
    if request.method == "POST":
        form = SpecialtyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('specialty_list')
    else:
        form = SpecialtyForm()
    return render(request, 'dental_management/specialty_form.html', {'form': form})

# Update an existing specialty
def specialty_update(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)
    if request.method == "POST":
        form = SpecialtyForm(request.POST, instance=specialty)
        if form.is_valid():
            form.save()
            return redirect('specialty_detail', pk=specialty.pk)
    else:
        form = SpecialtyForm(instance=specialty)
    return render(request, 'dental_management/specialty_form.html', {'form': form})

# Delete a specialty
def specialty_delete(request, pk):
    specialty = get_object_or_404(Specialty, pk=pk)
    if request.method == "POST":
        specialty.delete()
        return redirect('specialty_list')
    return render(request, 'dental_management/specialty_confirm_delete.html', {'specialty': specialty})
