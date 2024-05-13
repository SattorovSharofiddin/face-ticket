import uuid
from datetime import date

from django.db.models import BooleanField, CharField, Model, ImageField, DateField, UUIDField, BigIntegerField

nb = dict(null=True, blank=True)


# class BaseMeta:
#     ordering = ('-id',)


class BaseModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = CharField(max_length=255, **nb)
    last_name = CharField(max_length=255, **nb)
    three_name = CharField(max_length=255, **nb)
    job_title = CharField(max_length=255, **nb)
    passport_number = CharField(max_length=30, **nb)
    passport_date = CharField(max_length=20, **nb)
    passport_pin = CharField(max_length=20, **nb, unique=True)
    year_of_enter = CharField(max_length=20, **nb)
    main_image = ImageField(upload_to='images', **nb)
    birth_date = DateField(**nb)
    gender = BooleanField(**nb)
    created_at = DateField(auto_now_add=True)
    face_id = BigIntegerField(**nb)
    citizenship = CharField(max_length=255, **nb)
    home_address = CharField(max_length=255, **nb)
    province = CharField(max_length=255, **nb)
    district = CharField(max_length=255, **nb)

    class Meta:
        abstract = True

    @property
    def age(self):
        return int((date.today() - self.birth_date).days / 365.25)