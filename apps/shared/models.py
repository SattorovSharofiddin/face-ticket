import uuid
from datetime import date

from django.db.models import BooleanField, CharField, Model, ImageField, DateField, UUIDField, BigIntegerField

nb = dict(null=True, blank=True)


# class BaseMeta:
#     ordering = ('-id',)


class BaseModel(Model):
    # id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=100)
    description = CharField(max_length=255, **nb)
    created_at = DateField(auto_now_add=True)

    class Meta:
        abstract = True
