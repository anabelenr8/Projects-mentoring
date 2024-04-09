import json

from django.http.request import HttpRequest
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.reports.docs import post_report_description
from store.reports.generate.report import Report as ReportGenerator
from store.reports.generate.survey import Survey
from store.reports.models import Report as ReportModel
from store.serializers import SurveySerializer


@api_view(['GET'])
def get_api_survey_and_answers(request: HttpRequest) -> Response:
    return Response(
        status=200,
        data={
            'your_style': {
                'question': {
                    'key': 'your_style',
                    'display_name': 'How do you define your style?',
                },
                'answers': [
                    {'key': 'casual_comfortable',
                     'display_name': 'Casual and Comfortable'},

                    {'key': 'elegant_chic',
                     'display_name': 'Elegant and Chic'},

                    {'key': 'bohemian_relaxed',
                     'display_name': 'Bohemian and Relaxed'},

                    {'key': 'edgy_experimental',
                     'display_name': 'Edgy and Experimental'},

                    {'key': 'none_above', 'display_name': 'None of the above'},
                ],
            },
            'colour_palette': {
                'question': {
                    'key': 'colour_palette',
                    'display_name': 'Describe your colour palette?',
                },
                'answers': [
                    {'key': 'bright_vibrant',
                     'display_name': 'Bright and Vibrant'},

                    {'key': 'neutral_subdued',
                     'display_name': 'Neutral and Subdued'},

                    {'key': 'dark_muted', 'display_name': 'Dark and Muted'},

                    {'key': 'pastel_soft', 'display_name': 'Pastel and Soft'},

                    {'key': 'not_attention_colors',
                     'display_name': "I don't pay much attention to colors"},
                ],
            },
            'shopping_category': {
                'question': {
                    'key': 'shopping_category',
                    'display_name': 'What is your shopping category?',
                },
                'answers': [
                    {'key': 'tops', 'display_name': 'Tops'},

                    {'key': 'bottoms', 'display_name': 'Bottoms'},

                    {'key': 'dresses_jumpsuits',
                     'display_name': 'Dresses and Jumpsuits'},

                    {'key': 'accessories', 'display_name': 'Accessories'},

                    {'key': 'shoes', 'display_name': 'Shoes'},
                ],
            },
            'type_and_size': {
                'question': {
                    'key': 'type_and_size',
                    'display_name': 'What is your'
                                    ' type and size of measurements?',
                },
                'answers': [
                    {'key': 'type_uk', 'display_name': 'Type UK'},
                    {'key': 'type_us', 'display_name': 'Type US'},
                    {'key': 'type_eu', 'display_name': 'Type EU'},
                ],
            },
            'preference_on_recycling_materials': {
                'question': {
                    'key': 'preference_on_recycling_materials',
                    'display_name': 'What is your preference'
                                    ' on recycling materials?',
                },
                'answers': [
                    {'key': 'yes', 'display_name': 'Yes'},

                    {'key': 'limited_knowledge',
                     'display_name': 'Limited knowledge about it.'},

                    {'key': 'not_aware',
                     'display_name': "Not aware of sustainability efforts."},
                ],
                'choices': [
                    {'key': 'organic_materials',
                     'display_name': 'Organic Materials'},

                    {'key': 'recycling_materials',
                     'display_name': 'Recycling Materials'},

                    {'key': 'reuse_water', 'display_name': 'Reuse of Water'},

                    {'key': 'not_sure', 'display_name': 'Not Sure'},
                ],
            },
        },
    )


@swagger_auto_schema(
    method='POST',
    operation_description=post_report_description
)
@api_view(['POST'])
def post_report(request: HttpRequest):
    try:
        request_data = json.loads(request.body)
    except json.JSONDecodeError:
        return Response(
            data={'error': 'Invalid JSON'},
            status=400
        )

    serializer = SurveySerializer(data=request_data)
    serializer.is_valid(raise_exception=True)

    survey = Survey(
        Q1=serializer.validated_data['your_style'],
        Q2=serializer.validated_data['colour_palette'],
        Q3=serializer.validated_data['shopping_category'],
        Q4=serializer.validated_data['type_and_size'],
        Q5=serializer.validated_data['preference_on_recycling_materials']
    )

    report = ReportGenerator(survey=survey)
    report_text = report.generate()

    ReportModel.objects.create(text=report_text)

    return Response(
        data={'report_text': report_text},
        status=200
    )
