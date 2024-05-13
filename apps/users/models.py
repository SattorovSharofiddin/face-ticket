from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CharField, EmailField, BooleanField, Model

)
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = EmailField(unique=True)
    password = CharField(max_length=255)
    is_active = BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = CustomUserManager()
