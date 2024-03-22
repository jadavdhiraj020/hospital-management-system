from django.contrib import admin
from . import models


@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "specializations"]


@admin.register(models.Patient)
class PatienAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "phone"]
    list_per_page = 10


@admin.register(models.Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["doctor_name", "patient_name", "appointment_date", "status"]
    list_editable = ["status"]

    def doctor_name(self, appontment):
        return appontment.doctor.name

    def patient_name(self, appontment):
        return appontment.patient.name
