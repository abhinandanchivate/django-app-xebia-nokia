from mongoengine import connect
from django.conf import settings

def connect_to_mongo():
    connect(
        db=settings.MONGODB_SETTINGS['NAME'],
        host=settings.MONGODB_SETTINGS['HOST'],
        port=int(settings.MONGODB_SETTINGS['PORT']),
        username=settings.MONGODB_SETTINGS['USERNAME'],
        password=settings.MONGODB_SETTINGS['PASSWORD'],
        authentication_source=settings.MONGODB_SETTINGS['AUTH_SOURCE']
    )
