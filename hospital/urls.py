from django.urls import path
from .import views

urlpatterns = [
    path("", views.doctorDetails),
    path("patient", views.patientDetails),
    path("patient/<slug:slug>", views.patientIndivDetails, name='patient-detail'),
    path("doctorname", views.doctor_name_filter),
    path("patientname", views.patient_name_filter),
    ]
