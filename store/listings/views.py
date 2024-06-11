from rest_framework import serializers, viewsets

from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'listing_id',
            'title',
            'price',
            'currency_code',
            'description',
            'tags',
            'created_at',
            'updated_at'
        ]


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    lookup_field = 'listing_id'
