# response: requests.Response = requests.post(
#     'https://api.pythonic.me/v1/app/',
#     headers={
#         'Pythonic-Api-V1-Key': 'ApM8MUgSIFefsHDSSqoVKTHtEvZ'
#                                'ntOBlUW7gidnRtfazdFY4YD9EBxS'
#                                '54sdvIfD9NGASOJsaK2xeyXyZsw9BLw'
#     }
# )
# print(response.json())


import json

import requests

api_key = '736c751d-0ecd-426a-80cf-4a9ab782360e'
api_token = 'nBKd0EeSeNwtqau3KSzKMqUPsO7MgcLKMkP' \
            'IGmJHX3NzrvXmCxkkdqysWO5WZXwozKf61b65_bQsXomIiSIi9g'

api_v1_key = 'ApM8MUgSIFefsHDSSqoVKTHtEvZntOBl' \
             'UW7gidnRtfazdFY4YD9EBxS54sdvIfD9N' \
             'GASOJsaK2xeyXyZsw9BLw'


class ListingsRequest:

    def __init__(self, api_key, api_token):
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

    def create_app(self):
        url = 'https://api.pythonic.me/v1/app/'
        response = requests.post(url,
                                 headers={'Pythonic-Api-V1-Key': api_v1_key})
        return response.json()

    def get_digital_listings(self):
        url = 'https://api.pythonic.me/v1/listings/?listing_type=digital'
        response = requests.get(url, headers=self.set_headers())
        return response

    def get_soft_tag_listings(self):
        url = 'https://api.pythonic.me/v1/listings/?tag=soft'
        response = requests.get(url, headers=self.set_headers())
        return json.dumps(response.json(), indent=4)

    def get_usd_listings_under_20(self):
        url = 'https://api.pythonic.me/v1/listings/'
        params = {
            'currency_code': 'usd',
            'price_amount': 20
        }
        response = requests.get(url, headers=self.set_headers(), params=params)

        if response.status_code == 200:
            all_listings = response.json()

            filtered_listings = [listing for listing in all_listings if
                                 listing.get('currency_code') == 'usd'
                                 and listing.get('price_amount') is not None
                                 and float(listing['price_amount']) <= 20]

        return json.dumps(filtered_listings, indent=4)

        # if else filter listing empty list

    def get_blanket_search_listings(self):
        url = 'https://api.pythonic.me/v1/listings/?search=blanket'
        response = requests.get(url, headers=self.set_headers())
        return json.dumps(response.json(), indent=4)

    def get_cotton_eur_listings(self):
        url = 'https://api.pythonic.me/v1/listings/'
        params = {
            'tags': ['cotton'],
            'currency_code': 'eur'
        }
        response = requests.get(url, headers=self.set_headers(), params=params)

        if response.status_code == 200:
            all_listings = response.json()
            filtered_listings = [listing for listing in all_listings if
                                 listing.get('tags') == ['cotton']
                                 and listing.get('currency_code') == 'eur']

            return json.dumps(filtered_listings, indent=4)


listings_request = ListingsRequest(api_key=api_key, api_token=api_token)
app_creation_response = listings_request.create_app()
digital_listings = listings_request.get_digital_listings()
soft_tags = listings_request.get_soft_tag_listings()
usd_listing_under_20 = listings_request.get_usd_listings_under_20()
blanket = listings_request.get_blanket_search_listings()
cotton_eur = listings_request.get_cotton_eur_listings()

print("App Creation Response:", app_creation_response)
print("Digital Listings:", digital_listings)
print("Soft Tags:", soft_tags)
print("Listing under 20 USD:", usd_listing_under_20)
print("Blanket:", blanket)
print("Cotton EUR:", cotton_eur)
