import unittest
from unittest.mock import patch, Mock

import requests

from listings.base import ListingsRequest, hostname

listings_request = ListingsRequest(
    api_key='mocked-api-key',
    api_token='mocked-api-token',
    hostname=hostname
)


class TestListingsRequest(unittest.TestCase):
    def test_get_digital_listings__no_digital_listings(self):
        listings_request_mock = patch.object(
            target=requests,
            attribute='get',
            side_effect=[
                Mock(**{
                    'json.return_value': []
                })
            ]
        )
        with listings_request_mock:
            json_data = listings_request.get_digital_listings()

        self.assertEqual(json_data, [])

    def test_get_digital_listings__has_digital_listings(self):
        listings_request_mock = patch.object(
            target=requests,
            attribute='get',
            side_effect=[
                Mock(**{
                    'json.return_value': [
                        {
                            "listing_id": "1bc5b9dc-b609"
                                          "-4200-8378-d6b3c2271ae5",
                            "user_id": "2b79dbcb-f374-4d4f-a071-da82cf94d58e",
                            "shop_id": "a41a238a-f460-48f4-a364-098e6cb812a8",
                            "title": "Baby Bottles - Probably",
                            "description": "This is a reflect baby bottles."
                                           " Tell a figure girl. ",
                            "status": "private",
                            "quantity": 6,
                            "shop_section_id": 9,
                            "featured_rank": 10,
                            "listing_type": "digital",
                            "non_taxable": True,
                            "is_taxable": False,
                        }
                    ]
                })
            ]
        )

        with listings_request_mock:
            json_data = listings_request.get_digital_listings()

        self.assertEqual(json_data, [{
            "listing_id": "1bc5b9dc-b609-4200-8378-d6b3c2271ae5",
            "user_id": "2b79dbcb-f374-4d4f-a071-da82cf94d58e",
            "shop_id": "a41a238a-f460-48f4-a364-098e6cb812a8",
            "title": "Baby Bottles - Probably",
            "description": "This is a reflect"
                           " baby bottles. Tell a figure girl. ",
            "status": "private",
            "quantity": 6,
            "shop_section_id": 9,
            "featured_rank": 10,
            "listing_type": "digital",
            "non_taxable": True,
            "is_taxable": False,
        }])

    def test_get_soft_tag_listings__no_soft_tags(self):
        listings_request_mock = patch.object(
            target=requests,
            attribute='get',
            side_effect=[
                Mock(**{
                    'json.return_value': []
                })
            ]
        )
        with listings_request_mock:
            json_data = listings_request.get_soft_tag_listings()

        self.assertEqual(json_data, [])

    def test_get_soft_tag_listings__has_soft_tags(self):
        listings_request_mock = patch.object(
            target=requests,
            attribute='get',
            side_effect=[
                Mock(**{
                    'json.return_value': {
                        "tags": [
                            "cotton",
                            "baby",
                            "comfortable",
                            "machine washable",
                            "soft",
                            "wool",
                            "handmade"
                        ]
                    }
                })
            ]
        )
        with listings_request_mock:
            json_data = listings_request.get_soft_tag_listings()

        self.assertEqual(
            json_data,
            {
                "tags": [
                    "cotton",
                    "baby",
                    "comfortable",
                    "machine washable",
                    "soft",
                    "wool",
                    "handmade"
                ]
            }
        )

    def test_get_usd_listings_under_20__no_listings_under_20(self):
        listings_request_mock = patch.object(
            target=requests,
            attribute='get',
            side_effect=[
                Mock(**{
                    'json.return_value': []
                })
            ]
        )
        with listings_request_mock:
            json_data = listings_request.get_usd_listings_under_20()

        self.assertEqual(json_data, [])

    def test_get_usd_listings_under_20__has_listings_under_20(self):
        listings_request_mock = patch.object(
            target=requests,
            attribute='get',
            side_effect=[
                Mock(**{
                    'json.return_value': [
                        {'currency_code': 'usd', 'price_amount': 10},
                        {'currency_code': 'usd', 'price_amount': 15},
                        {'currency_code': 'usd', 'price_amount': 20},
                        {'currency_code': 'usd', 'price_amount': 25},
                        {'currency_code': 'usd', 'price_amount': 30}
                    ]
                })
            ]
        )
        with listings_request_mock:
            json_data = listings_request.get_usd_listings_under_20()

        expected_result = [
            {'currency_code': 'usd', 'price_amount': 10},
            {'currency_code': 'usd', 'price_amount': 15},
            {'currency_code': 'usd', 'price_amount': 20}
        ]

        self.assertEqual(json_data, expected_result)

    def test_get_blanket_search_listings__no_blanket_search(self):
        listings_request_mock = patch.object(
            target=requests,
            attribute='get',
            side_effect=[
                Mock(**{
                    'json.return_value': [{
                        "listing_id": "53731f65-8fa6-49ee-8a06-a575e84668ea",
                        "user_id": "2b79dbcb-f374-4d4f-a071-da82cf94d58e",
                        "shop_id": "a41a238a-f460-48f4-a364-098e6cb812a8",
                        "title": "Children's Toys - Significant",
                        "description": "This is a region children's toys."
                                       " Generation American total model"
                                       " common my participant. ",
                        "status": "private",
                        "quantity": 56,
                        "shop_section_id": 1,
                        "featured_rank": 58,
                        "listing_type": "physical",
                        "non_taxable": True,
                        "is_taxable": False,
                    }]
                })
            ]
        )
        with listings_request_mock:
            json_data = listings_request.get_usd_listings_under_20()

        self.assertEqual(json_data, [])

    def test_get_blanket_search_listings__has_blanket_search(self):
        listings_request_mock = patch.object(
            target=requests,
            attribute='get',
            side_effect=[
                Mock(**{
                    'json.return_value': [{
                        "listing_id": "0456bde6-da27-47ec-921b-27b731241a09",
                        "user_id": "2b79dbcb-f374-4d4f-a071-da82cf94d58e",
                        "shop_id": "a41a238a-f460-48f4-a364-098e6cb812a8",
                        "title": "Baby Blanket - Own",
                        "description": "This is a throughout baby blanket. "
                                       "Serve mind certain into. ",
                        "status": "public",
                        "quantity": 79,
                        "shop_section_id": 7,
                        "featured_rank": 70,
                        "listing_type": "digital",
                        "non_taxable": True,
                        "is_taxable": False,
                    }]
                })
            ]
        )
        with listings_request_mock:
            json_data = listings_request.get_blanket_search_listings()

        self.assertEqual(json_data, [{
            "listing_id": "0456bde6-da27-47ec-921b-27b731241a09",
            "user_id": "2b79dbcb-f374-4d4f-a071-da82cf94d58e",
            "shop_id": "a41a238a-f460-48f4-a364-098e6cb812a8",
            "title": "Baby Blanket - Own",
            "description": "This is a throughout baby blanket. "
                           "Serve mind certain into. ",
            "status": "public",
            "quantity": 79,
            "shop_section_id": 7,
            "featured_rank": 70,
            "listing_type": "digital",
            "non_taxable": True,
            "is_taxable": False,
        }])

    def test_get_cotton_eur_listings__no_cotton_eur_listings(self):
        listings_request_mock = patch.object(
            target=requests,
            attribute='get',
            side_effect=[
                Mock(**{
                    'json.return_value': [
                        {'title': 'Cotton Throw Pillow',
                         'description': 'Decorative pillow',
                         'tags': 'cotton',
                         'currency_code': 'usd'},
                        {'title': 'Wool Socks',
                         'description': 'Comfortable woolen socks',
                         'tags': 'wool',
                         'currency_code': 'eur'}
                    ]
                })
            ]
        )
        with listings_request_mock:
            json_data = listings_request.get_cotton_eur_listings()

        self.assertEqual(json_data, [])

    def test_get_cotton_eur_listings__has_cotton_eur(self):
        listings_request_mock = patch.object(
            target=requests,
            attribute='get',
            side_effect=[
                Mock(**{
                    'json.return_value': [
                        {
                            'title': 'Strollers - Traditional',
                            'description': 'This is a training strollers.',
                            'tags': ['cotton'],
                            'currency_code': 'eur'
                        }
                    ]
                })
            ]
        )
        with listings_request_mock:
            json_data = listings_request.get_cotton_eur_listings()

        self.assertEqual(json_data, [
            {
                'title': 'Strollers - Traditional',
                'description': 'This is a training strollers.',
                'tags': ['cotton'],
                'currency_code': 'eur'
            }
        ])


if __name__ == '__main__':
    unittest.main()
