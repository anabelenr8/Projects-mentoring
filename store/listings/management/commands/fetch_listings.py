import logging

from django.conf import settings
from django.core.management.base import BaseCommand

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
                    listing_object = Listing.objects.create(
                        title=listing.get('title'),
                        description=listing.get('description'),
                        price=listing.get('price_amount'),
                        currency_code=listing.get('currency_code'),
                        tags=listing.get('tags')
                    )

                    listing_object.uid = listing.get('listing_id')
                    listing_object.save()

            logger.info('Successfully fetched and saved listings to the database')
