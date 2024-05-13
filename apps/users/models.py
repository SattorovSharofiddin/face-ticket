from django.db import models
from django.db.models import Model

from shared.models import BaseModel


class Category(BaseModel):
    def __str__(self):
        return self.name


class Type(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Media(BaseModel):
    url = models.URLField()
    data = models.FileField(upload_to='media/')

    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
