from django.apps import AppConfig
from . import decorators


class DjangoModelRestoreConfig(AppConfig):
    name = 'django_model_restore'

    def ready(self):
        """
        By placing the archive model construction in the app_ready we are
        guaranteed that all the apps model files have been imported at this
        point. Importantly though, when this code is ran the AppRegistry has
        not been marked as ready so we can still register some models for this
        app.
        https://docs.djangoproject.com/en/2.2/ref/applications/#django.apps.apps.ready
        """
        decorators.make_soft_deletable()
