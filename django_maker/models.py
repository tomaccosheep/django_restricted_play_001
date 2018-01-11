from django.db import models

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class Play_Project(models.Model):
    def_id = get_random_string(length=32)
    unique_id = models.CharField(max_length=32, primary_key=True, default=def_id)
    con_001 = models.CharField(max_length=16, null=True)
    def __str__(self):
        return self.unique_id
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
