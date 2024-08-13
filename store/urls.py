from django.conf.urls.static import static
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from store import settings
from store.listings.views import ListingViewSet
from store.reports.views import get_api_survey_and_answers, post_report

schema_view = get_schema_view(
    openapi.Info(
        title='Store API',
        default_version='v1',
        description='Store API - The "Store - Survey and Report" is a'
                    ' Django REST API that collects user preferences'
                    ' on fashion and sustainability, covering style,'
                    ' color preferences, shopping habits, garment size,'
                    ' and recycling views. It aims to provide sustainable'
                    ' fashion brands with insights to align their products'
                    ' and practices with customer preferences.',

        terms_of_service='#',
        contact=openapi.Contact(email='ana.romero0501@gmailcom')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

viewsets = [
    {
        'prefix': r'api/listings',
        'viewset': ListingViewSet,
        'basename': 'listings'
    },
]
router = SimpleRouter()

for viewset in viewsets:
    router.register(
        prefix=viewset['prefix'],
        viewset=viewset['viewset'],
        basename=viewset['basename']
    )

urlpatterns = [
    path('api/survey/', get_api_survey_and_answers),
    path('api/report/', post_report, name='post_report_generation'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='docs')
]

urlpatterns = urlpatterns + router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
