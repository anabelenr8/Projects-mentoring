from typing import Dict

from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, viewsets

from .models import Listing


def swagger_docs(methods: Dict):
    def decorator(cls):
        for method, kwargs in methods.items():
            original_method = getattr(cls, method, None)
            if original_method:
                decorated_method = swagger_auto_schema(**kwargs)(
                    original_method)
                setattr(cls, method, decorated_method)
        return cls

    return decorator


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
    }
}


@swagger_docs(listing_methods)
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    lookup_field = 'uid'
