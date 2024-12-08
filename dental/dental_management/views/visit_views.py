from django.shortcuts import render, get_object_or_404, redirect
from dental_management.models import Visit, Appointment
from dental_management.forms.visit_forms import VisitForm

# List all visits for a patient
def visit_list(request, patient_id):
    visits = Visit.objects.filter(patient_id=patient_id)
    return render(request, 'dental_management/visit_list.html', {'visits': visits})

# Add a new visit
def visit_create(request, appointment_id=None):
    # If an appointment ID is passed, pre-fill the form with related appointment data
    if appointment_id:
        appointment = get_object_or_404(Appointment, id=appointment_id)
        initial_data = {
            'clinic': appointment.clinic,
            'doctor': appointment.doctor,
            'patient': appointment.patient,
        }
        form = VisitForm(initial=initial_data)
    else:
        form = VisitForm()

    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the visit list for the patient
            return redirect('visit_list', patient_id=form.cleaned_data['patient'].id)
    
    return render(request, 'dental_management/visit_form.html', {'form': form})