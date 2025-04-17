from django.apps import AppConfig
from django.conf import settings

class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
    
    def ready(self):
        import pages.signals  # importa os sinais
        # from mongoengine import connect

        # connect(
        #     db=settings.MONGODB_SETTINGS['db'],
        #     host=settings.MONGODB_SETTINGS['host'],
        #     port=settings.MONGODB_SETTINGS['port'],
        #     username=settings.MONGODB_SETTINGS['username'],
        #     password=settings.MONGODB_SETTINGS['password'],
        #     authentication_source=settings.MONGODB_SETTINGS.get('authentication_source', 'admin')
        # )
