from django.db import models
from django.db.models import Model


class Category(Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Media(Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
