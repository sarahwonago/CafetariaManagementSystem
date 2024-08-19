from django.apps import AppConfig


class CafetariaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myapps.cafetaria"

    def ready(self):
        # Import the signals to ensure they are registered
        import myapps.cafetaria.signals
