from django.apps import AppConfig


class channelizerConfig(AppConfig):
    name = 'channelizer'

    def ready(self):
        import channelizer.signals
