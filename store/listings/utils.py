from typing import Dict, Any, List

import requests
from django.conf import settings

from store.common.utils import log

JsonData = List[Dict[str, Any]]


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
            'Pythonic-Api-V1-Key': settings.PYTHONIC_API_V1_KEY,
            'X-Api-Key': self.api_key,
            'Authorization': f'Bearer {self.api_token}',
        }

    def create_app(self) -> dict[str, str]:
        response = requests.post(
            url=f'{self.hostname}/app/',
            headers={'Pythonic-Api-V1-Key': settings.PYTHONIC_API_V1_KEY}
        )
        response_data = response.json()
        if response.status_code == 201:
            return response_data
        else:
            log(
                details={
                    'message': f"Error creating app {response_data}"
                }
            )
            return {}

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
            data = res.json()
            if isinstance(data, dict) and 'detail' in data:
                log(
                    details={
                        'message': f"Error: {data['detail']}"
                    }
                )
                return []
            return data
        except requests.exceptions.RequestException as e:
            log(
                details={
                    'message': f'Exception: {e}'
                }
            )
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

    def get_usd_listings_under_20(self) -> JsonData:
        usd_listings: JsonData = (
            self.get_listings(
                params={
                    'currency_code': 'usd',
                    'price_amount': 20
                }
            )
        )
        return [
            listing for listing in usd_listings if
            listing.get('currency_code') == 'usd'
            and listing.get('price_amount') is not None
            and float(listing['price_amount']) <= 20.00
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
