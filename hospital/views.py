from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Patient
from .forms import DoctorForm, PatientForm
from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment
from .forms import AppointmentForm


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(
        request, "hospital/appointment_list.html", {"appointments": appointments}
    )


def appointment_add(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("appointment_list")
    else:
        form = AppointmentForm()
    return render(request, "hospital/appointment_add.html", {"form": form})


def home(request):
    appointments = Appointment.objects.all()
    return render(
        request, "hospital/index.html", {"appointments": appointments}
    )


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, "hospital/doctor_list.html", {"doctors": doctors})


def doctor_add(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("doctor_list")
    else:
        form = DoctorForm()
    return render(request, "hospital/doctor_add.html", {"form": form})


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "hospital/patient_list.html", {"patients": patients})


def patient_add(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patient_list")
    else:
        form = PatientForm()
    return render(request, "hospital/patient_add.html", {"form": form})


def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, "hospital/doctor_detail.html", {"doctor": doctor})


def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, "hospital/patient_detail.html", {"patient": patient})


def appointment_cancel(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        appointment.delete()
        return redirect("appointment_list")
    return render(
        request, "hospital/appointment_cancel.html", {"appointment": appointment}
    )
