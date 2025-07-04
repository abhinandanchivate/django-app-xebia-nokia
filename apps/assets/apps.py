# whenever we will start the application then it should connect to mongo db

from django.apps import AppConfig
from .mongo_connection import connect_to_mongo
class AssetsConfig(AppConfig):
    name = 'apps.assets'
    verbose_name = 'Assets Management'

    def ready(self):
        connect_to_mongo()