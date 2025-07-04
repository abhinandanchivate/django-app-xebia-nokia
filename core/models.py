
from django.db import models

class BaseEntity(models.Model):
    custom_id = models.CharField(max_length=20, unique=True, editable=False)
    entity_prefix = "Entity"
    class Meta:
        abstract = True
    def save(self, *args, **kwargs):
        if not self.custom_id:
            count = self.__class__.objects.count()+1
            # date in YYYYMMDD format add to custom_id
            from datetime import datetime
            date_str = datetime.now().strftime("%Y%m%d") 

            self.custom_id = f"{self.entity_prefix}-{date_str}-{count:04d}"
            super().save(*args, **kwargs)

    