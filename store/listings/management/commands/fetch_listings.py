from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from rest_framework import serializers

from store.common.fields import PriceField
from store.listings.models import Listing
from store.listings.utils import ListingsRequest, log


class Command(BaseCommand):
    help = 'Fetch listings from an external API and create db objects'

    def handle(self, *args, **options):
        listings_request = ListingsRequest(
            api_key=settings.PYTHONIC_API_KEY,
            api_token=settings.PYTHONIC_API_TOKEN,
            hostname=settings.PYTHONIC_API_HOSTNAME)

        data = []
        data.extend(listings_request.get_digital_listings())
        data.extend(listings_request.get_cotton_eur_listings())
        data.extend(listings_request.get_blanket_search_listings())
        data.extend(listings_request.get_soft_tag_listings())
        data.extend(listings_request.get_usd_listings_under_20())

        with atomic():
            for listing in data:
                uid = listing.get('listing_id')
                if not uid:
                    log({'level': 'error',
                         'message': f"Missing uid for listing:"
                                    f" {listing.get('title')}"})
                    continue

                price = listing.get('price_amount')
                if price is None:
                    log({'level': 'error',
                         'message': f"Missing price for listing:"
                                    f" {listing.get('title')}"})
                    continue

                try:
                    price = PriceField.validate_price(str(price))
                except serializers.ValidationError as e:
                    log({'level': 'error',
                         'message': f"Invalid price for listing:"
                                    f" {listing.get('title')}: {e}"})
                    continue

                try:
                    listing_object, \
                        created = Listing.objects.update_or_create(
                        uid=uid,
                        defaults={
                            'title': listing.get('title'),
                            'description': listing.get('description'),
                            'price': price,
                            'currency_code': listing.get('currency_code'),
                            'tags': listing.get('tags'),
                        }
                    )
                    if created:
                        log({'level': 'info',
                             'message': f"Created new listing:"
                                        f" {listing_object.title}"})
                    else:
                        log({'level': 'info',
                             'message': f"Updated existing listing:"
                                        f" {listing_object.title}"})
                except Exception as e:
                    log({'level': 'error',
                         'message': f"Error saving listing: {e}"})

            log({'level': 'info',
                 'message': 'Successfully fetched'
                            ' and saved listings to the database'})
