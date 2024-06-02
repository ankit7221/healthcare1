from django.apps import AppConfig

class NomanappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "nomanapp"
    
    def ready(self):
        import nomanapp.signals  # Change 'yourapp' to 'nomanapp'
