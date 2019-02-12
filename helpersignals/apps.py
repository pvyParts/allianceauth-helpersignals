from django.apps import AppConfig

class HelperSignalsConfig(AppConfig):
    name = 'helpersignals'
    label = 'helpersignals'

    def ready(self):
        import helpersignals.signals
