from django.apps import AppConfig


class RphusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rphusers'
    def ready(self) -> None:
        import rphusers.signals
