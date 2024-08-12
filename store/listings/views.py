from rest_framework import serializers, viewsets

from .models import Listing
from .utils import swagger_docs


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
        'responses': {200: ListingSerializer(many=True)}
    },
    'retrieve': {
        'operation_summary': "Retrieve a listing",
        'operation_description': "Retrieve a specific listing by ID",
        'tags': ["Listings"],
        'responses': {200: ListingSerializer()}
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
