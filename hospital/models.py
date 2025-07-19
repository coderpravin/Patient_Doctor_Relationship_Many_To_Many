from django.db import models
from django.utils.text import slugify

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"The Doctor name is {self.name} and specialization is {self.specialization}"
    
genderchoice = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
)   
 
class Patient(models.Model):
    name= models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=genderchoice)
    slug = models.SlugField(unique=True, blank=False, null=False)
    doctor = models.ManyToManyField(Doctor, related_name="patients")

    def __str__(self):
        doctor_name = [doc.name for doc in self.doctor.all()]
        return f"The Patient Name is {self.name} and doctor name is {doctor_name}"
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()


#Add Proxy-Models 
class DoctorProxy(Doctor):
    class Meta:
        proxy = True
        ordering = ["name"]
        verbose_name = 'doctor-name'

#Add Second Proxy Models
class PatientProxy(Patient):
    class Meta:
        proxy = True
        ordering = ["name"]
        verbose_name = 'patient by name'
    
