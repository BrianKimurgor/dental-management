from django.shortcuts import render, get_object_or_404, redirect
from dental_management.models import Visit, Doctor, Patient, Clinic, Procedure
from .forms import VisitForm 

# List all visits
def visit_list(request):
    visits = Visit.objects.all()
    return render(request, 'dental_management/visit_list.html', {'visits': visits})

# View visit details
def visit_detail(request, pk):
    visit = get_object_or_404(Visit, pk=pk)
    return render(request, 'dental_management/visit_detail.html', {'visit': visit})

# Create a new visit
def visit_create(request):
    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visit_list')  # Redirect to visit list after creating
    else:
        form = VisitForm()
    return render(request, 'dental_management/visit_form.html', {'form': form})

# Optionally, you could add update or delete functionality here, depending on requirements
