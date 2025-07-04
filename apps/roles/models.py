
from django.db import models
from core.models import BaseEntity
class Role(BaseEntity):

    entity_prefix= "Role"
    name= models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=1)
    permissions = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    