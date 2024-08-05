from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models

from store.common.fields import PriceField
from store.common.models import ProjectModel


def validate_currency(value):
    if value != 'eur':
        raise ValidationError(
            f'{value} is not a valid currency code. Only "eur" is allowed.',
            params={'value': value},
        )


class Listing(ProjectModel):
    title = models.CharField(max_length=255)
    price = PriceField()
    currency_code = models.CharField(
        max_length=3,
        validators=[validate_currency],
        default='eur'
    )
    description = models.TextField()
    tags = ArrayField(models.CharField(max_length=200), size=10)
