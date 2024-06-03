from django.db import models


class Listing(models.Model):
    listing_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    currency_code = models.CharField(max_length=3)
    description = models.TextField()
    tags = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
