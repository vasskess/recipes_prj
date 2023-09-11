from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "recipes_prj.accounts"

    def ready(self):
        import recipes_prj.accounts.signals
