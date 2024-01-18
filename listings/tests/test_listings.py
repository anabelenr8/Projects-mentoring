import unittest
from typing import Dict, Any
from unittest.mock import MagicMock, patch

from listings.base import ListingsRequest

listings_request = ListingsRequest(
    api_key='736c751d-0ecd-426a-80cf-4a9ab782360e',
    api_token='nBKd0EeSeNwtqau3KSzKMqUPsO7MgcLKMkP' \
              'IGmJHX3NzrvXmCxkkdqysWO5WZXwozKf61b65_bQsXomIiSIi9g',
    hostname='https://api.pythonic.me/v1'
)


class TestListingsRequest(unittest.TestCase):
    def mock_response_method(self, data: Dict[str, Any]):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = data
        return mock_response

    @patch('listings.base.ListingsRequest.get_digital_listings')
    def test_get_digital_listings(self, mock_get_listings):
        mock_res = self.mock_response_method(
            {'listing_type': 'digital'}
        )
        mock_get_listings.return_value = mock_res

        request = listings_request

        result = request.get_digital_listings()

        self.assertEqual(result, mock_res)

    @patch('listings.base.ListingsRequest.get_soft_tag_listings')
    def test_get_soft_tag_listings(self, mock_get_listings):
        mock_res = self.mock_response_method(
            {'tag': 'soft'}
        )
        mock_get_listings.return_value = mock_res

        request = listings_request

        result = request.get_soft_tag_listings()

        self.assertEqual(result, mock_res)

    @patch('listings.base.ListingsRequest.get_usd_listings_under_20')
    def test_get_usd_listings_under_20(self, mock_get_listings):
        params = [
            {'currency_code': 'usd', 'price_amount': 10},
            {'currency_code': 'usd', 'price_amount': 15},
            {'currency_code': 'usd', 'price_amount': 20},
            {'currency_code': 'usd', 'price_amount': 25},
            {'currency_code': 'usd', 'price_amount': 30}
        ]

        mock_res = [self.mock_response_method(data=param) for param in params
                    if param.get('currency_code') == 'usd'
                    and int(param['price_amount']) <= 20]

        mock_get_listings.return_value = mock_res

        request = listings_request

        result = request.get_usd_listings_under_20()

        expected_result = [
            {'currency_code': 'usd', 'price_amount': 10},
            {'currency_code': 'usd', 'price_amount': 15},
            {'currency_code': 'usd', 'price_amount': 20}
        ]

        self.assertEqual(result, mock_res, expected_result)

    @patch('listings.base.ListingsRequest.get_blanket_search_listings')
    def test_get_blanket_search_listings(self, mock_get_listings):
        mock_data = [
            {
                'title': 'Soft Wool Blanket',
                'description': 'Warm and cozy blanket',
            },
            {
                'title': 'Cotton Throw Pillow',
                'description': 'Decorative pillow',
            },
            {
                'title': 'Wool Socks',
                'description': 'Comfortable woolen socks',
            },
        ]
        filtered_data = [entry for entry in mock_data if
                         'blanket' in entry['title'] or
                         'blanket' in entry['description']]

        mock_res = [self.mock_response_method(data=entry)
                    for entry in filtered_data]

        mock_get_listings.return_value = mock_res

        request = listings_request

        result = request.get_blanket_search_listings()

        expected_result = [
            {
                'title': 'Soft Wool Blanket',
                'description': 'Warm and cozy blanket',
            }
        ]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
