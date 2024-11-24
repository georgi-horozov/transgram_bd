from django.contrib.auth import get_user_model
from django.db import models

from transgram.accounts.models import TransgramUser
from transgram.documents.validators_document import document_file_size

UserModel = get_user_model()


class Document(models.Model):

    reference = models.IntegerField(
        null=False,
        blank=False,
    )

    invoice = models.FileField(
        upload_to='invoices/',
        null=True,
        blank=True,
        validators=[document_file_size],
    )

    cmr = models.FileField(
        upload_to='cmrs/',
        null=True,
        blank=True,
        validators=[document_file_size],
    )

    additional_document = models.FileField(
        upload_to='additional_docs/',
        null=True,
        blank=True,
        validators=[document_file_size],
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


