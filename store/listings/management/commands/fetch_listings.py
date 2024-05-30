import json

from django.core.management.base import BaseCommand

from store.listings.utils import ListingsRequest


class Command(BaseCommand):
    help = 'Fetch listings from an external API and create a text file'

    def handle(self, *args, **options):
        api_key = 'your_api_key'  # replace with your actual API key
        api_token = 'your_api_token'  # replace with your actual API token
        hostname = 'https://api.pythonic.me/v1'

        listings_request = ListingsRequest(api_key, api_token, hostname)

        # Fetch data using ListingsRequest
        data = listings_request.get_digital_listings()  # Example method, you can call other methods as needed

        # Define the output file path
        output_file_path = 'listings_output.txt'

        # Write the data to a text file
        with open(output_file_path, 'w') as file:
            file.write(json.dumps(data, indent=4))

        self.stdout.write(self.style.SUCCESS(
            f'Successfully fetched listings and created {output_file_path}'))
