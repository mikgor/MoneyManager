from django.apps import AppConfig


class MoneymanagerappConfig(AppConfig):
    name = 'MoneyManagerApp'

    def ready(self):
        import MoneyManagerApp.signals
