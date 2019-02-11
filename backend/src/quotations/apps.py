from django.apps import AppConfig


class QuotationsConfig(AppConfig):
    name = 'quotations'

    def ready(self):
        from quotation_updater import updater
        updater.start()
