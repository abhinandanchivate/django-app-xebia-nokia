
from django.db import models
from core.models import BaseEntity

from apps.roles.models import Role
class Role(BaseEntity):

    entity_prefix= "Role"
    name= models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=1)
    permissions = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL,  null=True, blank=True, related_name='users')

    