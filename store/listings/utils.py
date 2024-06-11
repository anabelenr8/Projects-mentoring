import json
import os
from typing import Dict, Any, Union, List

import requests

api_key = os.getenv('API_KEY')
api_token = os.getenv('API_TOKEN')

api_v1_key = os.getenv('API_V1_KEY')

hostname = 'https://api.pythonic.me/v1'

JsonData = List[Dict[str, Any]]


def save_to_file(listings: Dict[str, Union[JsonData, str]]):
    directory = 'text_files'

    if not os.path.exists(directory):
        os.makedirs(directory)

    filepath = os.path.join(directory, listings['filename'])
    with open(filepath, 'w') as file:
        file.write(json.dumps(listings['data'], indent=4))


class ListingsRequest:

    def __init__(
            self,
            api_key: str,
            api_token: str,
            hostname: str
    ):
        self.hostname = hostname
        self.api_key = api_key
        self.api_token = api_token

    def set_headers(self):
        return {
            'Pythonic-Api-V1-Key': 'ApM8MUgSIFefsHDSSqoVKTHtEvZntOBl'
                                   'UW7gidnRtfazdFY4YD9EBxS54sdvIfD9N'
                                   'GASOJsaK2xeyXyZsw9BLw',

            'X-Api-Key': self.api_key,

            'Authorization': f'Bearer {self.api_token}',
        }

    def create_app(self) -> JsonData:
        response = requests.post(
            url=f'{self.hostname}/app/',
            headers={'Pythonic-Api-V1-Key': api_v1_key}
        )
        return response.json()

    def get_listings(
            self,
            params: Dict[str, str]
    ) -> JsonData:
        try:
            res: requests.Response = requests.get(
                url=f'{self.hostname}/listings/',
                headers=self.set_headers(),
                params=params
            )
            return res.json()
        except requests.exceptions.RequestException as e:
            print(f'exception: {e}')
            return []

    def get_digital_listings(self) -> JsonData:
        return self.get_listings(
            params={
                'listing_type': 'digital'
            }
        )

    def get_soft_tag_listings(self) -> JsonData:
        return self.get_listings(
            params={
                'tag': 'soft'
            }
        )

    # def get_usd_listings_under_20(self) -> JsonData:
    #     usd_listings: JsonData = (
    #         self.get_listings(
    #             params={
    #                 'currency_code': 'usd',
    #                 'price_amount': 20
    #             }
    #         )
    #     )
    #     return [
    #         listing for listing in usd_listings if
    #         listing.get('currency_code') == 'usd'
    #         and listing.get('price_amount') is not None
    #         and float(listing['price_amount']) <= 20.00
    #     ]

    def get_usd_listings_under_20(self) -> JsonData:
        usd_listings: JsonData = self.get_listings(
            params={
                'currency_code': 'usd',
                'price_amount': 20
            }
        )
        print("USD Listings:", usd_listings)
        return [
            listing for listing in usd_listings if
            isinstance(listing, dict) and
            listing.get('currency_code') == 'usd' and
            listing.get('price_amount') is not None and
            float(listing['price_amount']) <= 20.00
        ]

    def get_blanket_search_listings(self) -> JsonData:
        return self.get_listings(
            params={
                'search': 'blanket'
            }
        )

    def get_cotton_eur_listings(self) -> JsonData:
        cotton_listings: JsonData = (
            self.get_listings(
                params={
                    'tags': ['cotton'],
                    'currency_code': 'eur'
                }
            )
        )
        return [
            listing for listing in cotton_listings if
            listing.get('tags') == ['cotton']
            and listing.get('currency_code') == 'eur'
        ]
