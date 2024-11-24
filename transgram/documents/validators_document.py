from django.core.exceptions import ValidationError


def document_file_size(value):
    max_document_size = 5 * 1024 * 1024
    if value.size > max_document_size:
        raise ValidationError(f"The maximum file size is {max_document_size / (1024 * 1024)} KB")