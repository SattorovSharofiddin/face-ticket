from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.db.models import ForeignKey, CASCADE, URLField, FileField

from shared.models import BaseModel


class Category(MPTTModel, BaseModel):
    parent = TreeForeignKey('self', on_delete=CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name


class Media(BaseModel):
    url = URLField()
    data = FileField(upload_to='media/')

    type = ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.name
