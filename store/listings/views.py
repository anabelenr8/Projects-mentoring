from drf_yasg.utils import swagger_auto_schema
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

    @swagger_auto_schema(
        operation_summary="List all listings",
        operation_description="Retrieve a list of all listings in the database",
        tags=["Listings"],
        responses={200: ListingSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a listing",
        operation_description="Retrieve a specific listing by ID",
        tags=["Listings"],
        responses={200: ListingSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
