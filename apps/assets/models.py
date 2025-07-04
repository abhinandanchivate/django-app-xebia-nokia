
from mongoengine import Document, StringField, IntField, DateTimeField, ListField, EmbeddedDocument, DecimalField

class Asset(Document):
    name =StringField(required=True,max_length=100)
    type = StringField(required=True,max_length=50)
    value=DecimalField(required=True, precision=2)
    assigned_to = StringField(max_length=100, null=True)
    status = StringField(choices=['available', 'assigned', 'maintenance', 'retired'], default='available')
    meta = {
        'collection':'assets',
        'ordering': ['-id']
    }
