from django.apps import AppConfig


class RatemConfig(AppConfig):
    name = 'ratem'

    def ready(self):
    	super(RatemConfig, self).ready()
    	from . import signals
