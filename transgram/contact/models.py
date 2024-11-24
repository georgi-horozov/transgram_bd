from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Contact(models.Model):
    MAX_FIRST_NAME_LENGTH = 50
    MAX_LAST_NAME_LENGTH = 50

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    phone_number = models.CharField(
        max_length=15,
        null=False,
        blank=False,
    )

    message = models.TextField(
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete = models.SET_NULL,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)