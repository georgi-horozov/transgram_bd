from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transgram.accounts'

    def ready(self):
        import transgram.accounts.signals
