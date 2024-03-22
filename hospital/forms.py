from django import forms
from .models import Doctor, Patient, Appointment


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ("name", "specializations")


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ("name", "age", "phone")


class AppointmentForm(forms.ModelForm):
    appointment_date = forms.DateField(
        input_formats=["%Y-%m-%d"], widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Appointment
        fields = ["doctor", "patient", "appointment_date"]
