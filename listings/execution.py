from listings.base import ListingsRequest, \
    api_key, api_token, hostname, save_to_file

api = ListingsRequest(
    api_key=api_key,
    api_token=api_token,
    hostname=hostname
)
app_creation_response = api.create_app()

for listings in [
    {
        'data': api.get_digital_listings(),
        'filename': 'digital_listings_txt'
    },
    {
        'data': api.get_soft_tag_listings(),
        'filename': 'soft_tags_txt'
    },
    {
        'data': api.get_usd_listings_under_20(),
        'filename': 'usd_listing_under_20_txt'
    },
    {
        'data': api.get_blanket_search_listings(),
        'filename': 'blanket_txt'
    },
    {
        'data': api.get_cotton_eur_listings(),
        'filename': 'cotton_eur_txt'
    },
]:
    save_to_file(listings=listings)
