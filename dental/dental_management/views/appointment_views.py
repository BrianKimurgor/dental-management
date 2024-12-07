from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from dental_management.models import Appointment, Clinic, Doctor, Patient, Procedure
# from .forms import AppointmentForm  # You can create this form for appointment creation

# List all appointments
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'dental_management/appointment_list.html', {'appointments': appointments})

# View appointment details
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'dental_management/appointment_detail.html', {'appointment': appointment})

# Create a new appointment
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')  # Redirect to appointment list after creating
    else:
        form = AppointmentForm()
    return render(request, 'dental_management/appointment_form.html', {'form': form})

# Optionally, you could add update or delete functionality here, depending on requirements
