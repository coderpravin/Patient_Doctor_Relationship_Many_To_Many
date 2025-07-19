from django.shortcuts import render
from .models import Patient, Doctor, DoctorProxy, PatientProxy
# Create your views here.

def doctorDetails(request):
    doctors = Doctor.objects.all()

    #Create Session Here
    if doctors.exists():
        request.session['doctor_id'] = doctors.first().id
        print(f"Doctor Id Store in session Id :{request.session['doctor_id']}")
    
    return render(request, "hospital/doctor_info.html", {'doctors':doctors})

def doctor_name_filter(request):
    doctors = DoctorProxy.objects.all()
    return render(request, "hospital/doctor_name_filter.html", {'doctors':doctors})

def patientDetails(request):
    patients = Patient.objects.prefetch_related('doctor').all()
    if patients:
        last_patient = patients.last()
        select_doctor_id = [doc.id for doc in last_patient.doctor.all()]
        request.session["selected_doctors"] = select_doctor_id
        print(f"The doctor session: {request.session['selected_doctors']}")

    for p in patients:
        p.doc_name = "".join([doc.name for doc in p.doctor.all()])
        print(f"The doctor name is {p.doc_name}")
    return render(request, "hospital/patient_info.html", {'patients':patients})


def patientIndivDetails(request, slug):
    patients = Patient.objects.get(slug=slug)
    print(patients)
    return render(request, "hospital/individual_patient.html", {"patients":patients})

def patient_name_filter(request):
    patients = PatientProxy.objects.all()
    for p in patients:
        p.doc_name = [doc.name for doc in p.doctor.all()]
    return render(request, "hospital/patient_name_filter.html", {'patients':patients})


