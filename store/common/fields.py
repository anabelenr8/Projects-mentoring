from decimal import Decimal, InvalidOperation

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework import serializers

max_price_value = 4800000


class PriceField(models.IntegerField):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('validators', [
            MinValueValidator(1),
            MaxValueValidator(max_price_value)
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
            if not (1 <= price_float <= max_price_value):
                raise serializers.ValidationError(
                    f'Price must be between 1 and {max_price_value}.'
                )

            return int(price_float * 100)
        except (ValueError, InvalidOperation):
            raise serializers.ValidationError('Invalid price format.')

    def get_prep_value(self, value):
        if isinstance(value, str):
            value = self.validate_price(value)
        elif isinstance(value, Decimal):
            value = int(value * 100)
        return super().get_prep_value(value)
