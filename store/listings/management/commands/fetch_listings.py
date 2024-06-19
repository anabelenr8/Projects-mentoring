import os

from django.core.management.base import BaseCommand

from store.listings.utils import ListingsRequest, save_to_file


class Command(BaseCommand):
    help = 'Fetch listings from an external API and create text files'

    def handle(self, *args, **options):
        api_key = os.getenv('API_KEY')
        api_token = os.getenv('API_TOKEN')
        hostname = 'https://api.pythonic.me/v1'

        listings_request = ListingsRequest(api_key, api_token, hostname)

        listings_data = [
            {
                'data': listings_request.get_digital_listings(),
                'filename': 'digital_listings.txt'
            },
            {
                'data': listings_request.get_soft_tag_listings(),
                'filename': 'soft_tags.txt'
            },
            {
                'data': listings_request.get_usd_listings_under_20(),
                'filename': 'usd_listings_under_20.txt'
            },
            {
                'data': listings_request.get_blanket_search_listings(),
                'filename': 'blanket.txt'
            },
            {
                'data': listings_request.get_cotton_eur_listings(),
                'filename': 'cotton_eur.txt'
            },
        ]

        for listings in listings_data:
            save_to_file(listings=listings)
