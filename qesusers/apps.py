from django.apps import AppConfig


class QesusersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qesusers'
   

    def ready(self):
        import qesusers.signals