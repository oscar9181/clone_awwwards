from django.apps import AppConfig


class AwwwardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'awwwards'
    def ready(self):
        import  awwwards.signals





