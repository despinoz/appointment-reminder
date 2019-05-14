from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "animus.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import animus.users.signals  # noqa F401
        except ImportError:
            pass
