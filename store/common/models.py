import uuid
from decimal import Decimal, InvalidOperation

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework import serializers


class TimestampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProjectModel(TimestampedModel):
    class Meta:
        abstract = True

    uid = models.UUIDField(unique=True, null=False, default=uuid.uuid4)


class PriceField(models.IntegerField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('validators', [
            MinValueValidator(1),
            MaxValueValidator(48000)
        ])
        super().__init__(*args, **kwargs)

    @staticmethod
    def format_price(price: int) -> str:
        n = Decimal(price) / Decimal('100')
        return str(n)

    @staticmethod
    def validate_price(value: str) -> int:
        try:
            price_float = Decimal(value)

            if not (1 <= price_float <= 48000):
                raise serializers.ValidationError(
                    'Price must be between 1 and 48000.'
                )

            return int(price_float * 100)
        except (ValueError, InvalidOperation):
            raise serializers.ValidationError('Invalid price format.')
