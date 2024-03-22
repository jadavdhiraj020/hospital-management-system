from django.urls import path
from hospital import views

urlpatterns = [
    path("https://jadavdhiraj020.github.io/hospital-management-system/", views.home, name="home"),
    path("doctor/list/", views.doctor_list, name="doctor_list"),
    path("doctor/<int:doctor_id>/", views.doctor_detail, name="doctor_detail"),
    path("doctor/add/", views.doctor_add, name="doctor_add"),
    path("patient/list/", views.patient_list, name="patient_list"),
    path("patient/<int:patient_id>/", views.patient_detail, name="patient_detail"),
    path("patient/add/", views.patient_add, name="patient_add"),
    path("appointment/list/", views.appointment_list, name="appointment_list"),
    path("appointment/add/", views.appointment_add, name="appointment_add"),
    path("appointment/<int:appointment_id>/cancel/", views.appointment_cancel, name="appointment_cancel"),
]
