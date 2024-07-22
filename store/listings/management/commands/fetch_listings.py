import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from rest_framework import serializers

from store.common.fields import PriceField
from store.listings.models import Listing
from store.listings.utils import ListingsRequest

logger = logging.getLogger('listings')


class Command(BaseCommand):
    help = 'Fetch listings from an external API and create db objects'

    def handle(self, *args, **options):
        listings_request = ListingsRequest(
            api_key=settings.PYTHONIC_API_KEY,
            api_token=settings.PYTHONIC_API_TOKEN,
            hostname=settings.PYTHONIC_API_HOSTNAME)

        listings_data = [
            {
                'data': listings_request.get_digital_listings(),
            },
            {
                'data': listings_request.get_soft_tag_listings(),
            },
            {
                'data': listings_request.get_usd_listings_under_20(),
            },
            {
                'data': listings_request.get_blanket_search_listings(),
            },
            {
                'data': listings_request.get_cotton_eur_listings(),
            },
        ]

        from django.db.transaction import atomic
        with atomic():
            for listings in listings_data:
                for listing in listings['data']:
                    uid = listing.get('listing_id')
                    if not uid:
                        logger.error(f"Missing uid for listing: {listing.get('title')}")
                        continue

                    price = listing.get('price_amount')
                    if price is None:
                        logger.error(f"Missing price for listing: {listing.get('title')}")
                        continue

                    try:
                        price = PriceField.validate_price(str(price))
                    except serializers.ValidationError as e:
                        logger.error(f"Invalid price for listing: {listing.get('title')}: {e}")
                        continue

                    try:
                        listing_object, created = Listing.objects.update_or_create(
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
                            logger.info(f"Created new listing: {listing_object.title}")
                        else:
                            logger.info(f"Updated existing listing: {listing_object.title}")
                    except Exception as e:
                        logger.error(f"Error saving listing: {e}")

            logger.info('Successfully fetched and saved listings to the database')
