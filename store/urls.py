from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from store.reports.views import get_api_survey_and_answers
from store.reports.views import post_report

schema_view = get_schema_view(
    openapi.Info(
        title='Store API',
        default_version='v1',
        description='Store API - for Python learning',
        terms_of_service='#',
        contact=openapi.Contact(email='ana.romero0501@gmailcom')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('api/survey/', get_api_survey_and_answers),
    path('api/report/', post_report, name='post_report_generation'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='docs')
]
