from django.shortcuts import render, get_object_or_404, redirect
from dental_management.models import Appointment
from dental_management.forms.appointment_form import AppointmentForm

# List all appointments for a patient
def appointment_list(request, patient_id):
    appointments = Appointment.objects.filter(patient_id=patient_id)
    return render(request, 'dental_management/appointment_list.html', {'appointments': appointments})

# Schedule a new appointment
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST, user=request.user)
        if form.is_valid():
            # Check for doctor availability
            doctor = form.cleaned_data['doctor']
            date_time = form.cleaned_data['date_time']
            if Appointment.objects.filter(doctor=doctor, date_time=date_time).exists():
                form.add_error('date_time', 'This time slot is already booked for the selected doctor.')
            else:
                appointment = form.save()
                patient_id = appointment.patient.id  # Ensure patient ID is correctly saved

                # Redirect with the correct patient_id to appointment_list
                return redirect('appointment_list', patient_id=patient_id)
    else:
        form = AppointmentForm()

    return render(request, 'dental_management/appointment_form.html', {'form': form})
