from django.db import models
from django.db.models import Model


class Category(Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
