from django.core.exceptions import ValidationError


def profile_photo_size(value):
    max_photo_size = 1 * 1024 * 1024
    if value.size > max_photo_size:
        raise ValidationError("Your photo must be less thаn 1 MB!")