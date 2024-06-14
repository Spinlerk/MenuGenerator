from django.apps import AppConfig


class GeneratorConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Generator"

    def ready(self):  # ensure registration and activation of signals
        import Generator.signals

from django.apps import AppConfig

class GeneratorConfig(AppConfig):
    name = 'Generator'

    def ready(self):
        import Generator.signals