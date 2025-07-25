# Generated by Django 5.2.4 on 2025-07-19 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_doctorproxy'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProxy',
            fields=[
            ],
            options={
                'verbose_name': 'patient by name',
                'ordering': ['name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('hospital.patient',),
        ),
    ]
