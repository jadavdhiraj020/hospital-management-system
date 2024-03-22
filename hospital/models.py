from django.db import models
from django.core.exceptions import ValidationError


class Doctor(models.Model):
    SPECIALIZATIONS_CHOICES = [
        ("A", "Audiologists"),
        ("C", "Cardiologists"),
        ("G", "Gynecologist"),
    ]

    name = models.CharField(max_length=255)
    specializations = models.CharField(max_length=1, choices=SPECIALIZATIONS_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_specializations_display()})"

    class Meta:
        ordering = ["id"]


class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class Appointment(models.Model):
    APPOINMENT_STATUS = [
        ("P", "Pending"),
        ("C", "Complete"),
    ]

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    status = models.CharField(max_length=1, choices=APPOINMENT_STATUS, default="P")

    def checking(self):
        # Check if the doctor is available on the appointment date
        existing_appointments = Appointment.objects.filter(
            doctor=self.doctor, appointment_date=self.appointment_date
        )
        if existing_appointments.exists():
            raise ValidationError("Doctor is not available on this date.")

    def save(self, *args, **kwargs):
        self.checking()  # Call the clean method before saving
        super().save(*args, **kwargs)
