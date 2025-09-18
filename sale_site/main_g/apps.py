from django.apps import AppConfig


class MainGConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_g'

    def ready(self):
        import main_g.signals
