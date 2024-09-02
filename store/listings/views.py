from drf_yasg import openapi
from rest_framework import serializers, viewsets

from .models import Listing
from .utils import swagger_docs

example_listing_response = {
    "id": 1,
    "title": "Baby Bottles - Probably",
    "price": "1500",
    "currency_code": "usd",
    "description": "This is a reflect baby bottles. Tell a figure girl.",
    "tags": ["soft", "wool"],
    "created_on": "2023-08-22T10:00:00Z",
    "updated_on": "2023-08-22T12:00:00Z"
}


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'price',
            'currency_code',
            'description',
            'tags',
            'created_on',
            'updated_on'
        ]


listing_methods = {
    'list': {
        'operation_summary': "List all listings",
        'operation_description': "Retrieve a list"
                                 " of all listings in the database",
        'tags': ["Listings"],
        'responses': {
            200: openapi.Response(
                description="A list of listings",
                examples={
                    "application/json": [example_listing_response]
                },
                schema=ListingSerializer(many=True)
            )
        }
    },
    'retrieve': {
        'operation_summary': "Retrieve a listing",
        'operation_description': "Retrieve a specific listing by ID",
        'tags': ["Listings"],
        'parameters': [
            openapi.Parameter(
                'uid',
                openapi.IN_PATH,
                description="UUID of the listing",
                type=openapi.TYPE_STRING,
                required=True,
                example="9b8f4f2c-8097-4b5e-9d2c-928d5fcf5c6b"
            ),
        ],
        'responses': {
            200: openapi.Response(
                description="A single listing",
                examples={
                    "application/json": example_listing_response
                },
                schema=ListingSerializer(),
            )
        }
    },
    'create': {
        'auto_schema': None
    },
    'update': {
        'auto_schema': None
    },
    'partial_update': {
        'auto_schema': None
    },
    'destroy': {
        'auto_schema': None
    }
}


@swagger_docs(listing_methods)
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    lookup_field = 'uid'
