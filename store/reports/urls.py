from django.contrib import admin
from django.urls import path

from store.reports.views import get_api_survey_and_answers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/api/survey/', get_api_survey_and_answers)
]
