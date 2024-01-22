import unittest
from unittest.mock import patch

from listings.base import ListingsRequest, api_key, api_token, hostname

listings_request = ListingsRequest(
    api_key=api_key,
    api_token=api_token,
    hostname=hostname
)


class TestListingsRequest(unittest.TestCase):
    @patch('listings.base.ListingsRequest.get_digital_listings')
    def test_get_digital_listings(self, mock_get_listings):
        expected_result = [{'listing_type': 'digital'}]

        mock_get_listings.return_value = expected_result

        request = listings_request

        result = request.get_digital_listings()

        self.assertEqual(result, expected_result)

    @patch('listings.base.ListingsRequest.get_soft_tag_listings')
    def test_get_soft_tag_listings(self, mock_get_listings):
        expected_result = [{'tag': 'soft'}]

        mock_get_listings.return_value = expected_result

        request = listings_request

        result = request.get_soft_tag_listings()

        self.assertEqual(result, expected_result)

    @patch('listings.base.ListingsRequest.get_usd_listings_under_20')
    def test_get_usd_listings_under_20(self, mock_get_listings):
        expected_data_contains_listings_under_20 = [
            {'currency_code': 'usd', 'price_amount': 10},
            {'currency_code': 'usd', 'price_amount': 15},
            {'currency_code': 'usd', 'price_amount': 20},
        ]

        expected_data_does_not_contains_listings_under_20 = [
            {'currency_code': 'usd', 'price_amount': 10},
            {'currency_code': 'usd', 'price_amount': 15},
            {'currency_code': 'usd', 'price_amount': 20},
            {'currency_code': 'usd', 'price_amount': 25},
            {'currency_code': 'usd', 'price_amount': 30}
        ]

        mock_get_listings.side_effect = \
            [expected_data_contains_listings_under_20,
             expected_data_does_not_contains_listings_under_20]

        request = listings_request

        result = request.get_usd_listings_under_20()

        expected_result = [item for item in
                           expected_data_contains_listings_under_20 if
                           item['price_amount'] <= 20]

        self.assertEqual(result, expected_result)

    @patch('listings.base.ListingsRequest.get_blanket_search_listings')
    def test_get_blanket_search_listings(self, mock_get_listings):
        expected_result_contains_blanket = [
            {'title': 'Soft Wool Blanket',
             'description': 'Warm and cozy blanket', }
        ]

        expected_result_does_not_contain_blanket = [
            {'title': 'Cotton Throw Pillow',
             'description': 'Decorative pillow', }
        ]

        mock_get_listings.side_effect = \
            [expected_result_contains_blanket,
             expected_result_does_not_contain_blanket]

        request = listings_request

        result_contains_blanket = request.get_blanket_search_listings()
        self.assertEqual(result_contains_blanket,
                         expected_result_contains_blanket)

        result_does_not_contain_blanket = request.get_blanket_search_listings()
        self.assertEqual(result_does_not_contain_blanket,
                         expected_result_does_not_contain_blanket)

    @patch('listings.base.ListingsRequest.get_cotton_eur_listings')
    def test_get_cotton_eur_listings(self, mock_get_listings):
        expected_result_meets_criteria = [
            {'title': 'Soft Wool Blanket',
             'description': 'Warm and cozy blanket',
             'tag': 'cotton',
             'currency_code': 'eur'}
        ]

        expected_result_does_not_meet_criteria = [
            {'title': 'Cotton Throw Pillow',
             'description': 'Decorative pillow',
             'tag': 'cotton',
             'currency_code': 'usd'},
            {'title': 'Wool Socks',
             'description': 'Comfortable woolen socks',
             'tag': 'wool',
             'currency_code': 'eur'}
        ]

        mock_get_listings.side_effect = \
            [expected_result_meets_criteria,
             expected_result_does_not_meet_criteria]

        request = listings_request

        result_meets_criteria = request.get_cotton_eur_listings()
        self.assertEqual(result_meets_criteria, expected_result_meets_criteria)

        result_does_not_meet_criteria = request.get_cotton_eur_listings()
        self.assertEqual(result_does_not_meet_criteria,
                         expected_result_does_not_meet_criteria)


if __name__ == '__main__':
    unittest.main()
