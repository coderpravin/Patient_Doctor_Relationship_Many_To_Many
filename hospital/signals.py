from .models import Patient, Doctor
from django.db.models.signals import post_save, post_delete,post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_save, sender=Doctor)
def doctor_created(sender, instance , created, **kwargs):
    if created:
        print("The new doctor is created", instance.name)

@receiver(post_delete, sender=Doctor)
def doctor_deleted(sender, instance, **kwargs):
    print(f"The doctor record is delete {instance.name}")

@receiver(post_save,sender=Patient)
def patient_created(sender, instance, created, **kwargs):
    if created:
        print(f"The New Patient Record Created {instance.name} and {instance.gender}" )

@receiver(post_migrate)
def create_group(sender, **kwargs):
    group, created = Group.objects.get_or_create(name="Doctor")
    if created:
        print("Migrations Done")




