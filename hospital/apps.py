from django.apps import AppConfig


class PersonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hospital'

    def ready(self):
        import hospital.signals
