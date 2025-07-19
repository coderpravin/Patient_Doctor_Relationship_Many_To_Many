from django.contrib import admin
from .models import Doctor, Patient, DoctorProxy, PatientProxy
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)

@admin.register(DoctorProxy)
class DoctorProxy(admin.ModelAdmin):
    list_display = ["name", "specialization"]

@admin.register(PatientProxy)
class PatientProxy(admin.ModelAdmin):

    list_display = ["name", "gender", "doctor_list"]

    def doctor_list(self, patient):
        doctorName = "".join([doc.name for doc in patient.doctor.all()])
        return doctorName
    
