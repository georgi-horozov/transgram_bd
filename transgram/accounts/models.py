from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from transgram.accounts.managers import TransgramUserManager
from transgram.accounts.validators import profile_photo_size


class TransgramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )


    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )


    USERNAME_FIELD = "email"

    objects = TransgramUserManager()


class Profile(models.Model):
    MAX_LENGTH_COMPANY_NAME = 50
    MAX_VAT_LENGTH = 20
    MAX_ADDRESS_LENGTH = 150

    company_name = models.CharField(
        max_length=MAX_LENGTH_COMPANY_NAME,
        null=True,
        blank=True,
    )

    vat = models.CharField(
        max_length=MAX_VAT_LENGTH,
        null=True,
        blank=True,
        unique=True,
    )

    address = models.TextField(
        max_length=MAX_ADDRESS_LENGTH,
        null=True,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        # validators=[RegexValidator(r'^\+?1?\d{9,15}$',
        #                            message="Phone number must be in the format: '+999999999'. Up to 15 digits allowed.")]
    )

    profile_photo = models.ImageField(
        upload_to="mediafiles/photos",
        validators=[profile_photo_size],
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        TransgramUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

