import json

from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

from store.reports.models import Report as ReportModel
from store.serializers import SurveySerializer
from survey_report.report import Survey, Report as ReportGenerator


@require_http_methods(['GET'])
def get_api_survey_and_answers(request: HttpRequest) -> JsonResponse:
    return JsonResponse(
        status=200,
        data={
            'your_style': {
                'question': {
                    'key': 'how_do_you_define_your_style',
                    'display_name': 'How do you define your style?',
                },
                'answers': [
                    {'key': 'casual_comfortable', 'display_name': 'casual and comfortable'},
                    {'key': 'elegant_chic', 'display_name': 'elegant and chic'},
                    {'key': 'bohemian_relaxed', 'display_name': 'bohemian and relaxed'},
                    {'key': 'edgy_experimental', 'display_name': 'edgy and experimental'},
                    {'key': 'none_above', 'display_name': 'none of the above'},
                ],
            },
            'colour_palette': {
                'question': {
                    'key': 'describe_your_colour_palette',
                    'display_name': 'Describe your colour palette?',
                },
                'answers': [
                    {'key': 'bright_vibrant', 'display_name': 'bright and vibrant'},
                    {'key': 'neutral_subdued', 'display_name': 'neutral and subdued'},
                    {'key': 'dark_muted', 'display_name': 'dark and muted'},
                    {'key': 'pastel_soft', 'display_name': 'pastel and soft'},
                    {'key': 'not_attention_colors', 'display_name': "I don't pay much attention to colors"},
                ],
            },
            'shopping_category': {
                'question': {
                    'key': 'what_is_your_shopping_category',
                    'display_name': 'What is your shopping category?',
                },
                'answers': [
                    {'key': 'tops', 'display_name': 'Tops'},
                    {'key': 'bottoms', 'display_name': 'Bottoms'},
                    {'key': 'dresses_jumpsuits', 'display_name': 'Dresses and Jumpsuits'},
                    {'key': 'accessories', 'display_name': 'Accessories'},
                    {'key': 'shoes', 'display_name': 'Shoes'},
                ],
            },
            'type_and_size': {
                'question': {
                    'key': 'what_is_your_type_and_size_of_measurements',
                    'display_name': 'What is your type and size of measurements?',
                },
                'answers': [
                    {'key': 'type_uk', 'display_name': 'Type UK'},
                    {'key': 'type_us', 'display_name': 'Type US'},
                    {'key': 'type_eu', 'display_name': 'Type EU'},
                ],
            },
            'preference_on_recycling_materials': {
                'question': {
                    'key': 'what_is_your_preference_on_recycling_materials',
                    'display_name': 'What is your preference on recycling materials?',
                },
                'answers': [
                    {'key': 'yes', 'display_name': 'yes'},
                    {'key': 'limited_knowledge', 'display_name': 'limited knowledge about it.'},
                    {'key': 'not_aware', 'display_name': "not aware of sustainability efforts."},
                ],
                'choices': [
                    {'key': 'organic_materials', 'display_name': 'Organic Materials'},
                    {'key': 'recycling_materials', 'display_name': 'Recycling Materials'},
                    {'key': 'reuse_water', 'display_name': 'Reuse of Water'},
                    {'key': 'not_sure', 'display_name': 'Not Sure'},
                ],
            },
        },
    )


@swagger_auto_schema(
    method='POST',
    operation_description='Processes a POST request with user survey responses,'
                          ' generating a personalized style report. Validates'
                          ' input, saves the report, and returns the report'
                          ' text. Returns errors for invalid JSON or data.'
)
@api_view(['POST'])
def post_report_generation(request):
    try:
        request_data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    serializer = SurveySerializer(data=request_data)
    if serializer.is_valid(raise_exception=True):
        user_selected_answers = serializer.validated_data

        survey = Survey(
            Q1=user_selected_answers['your_style'],
            Q2=user_selected_answers['colour_palette'],
            Q3=user_selected_answers['shopping_category'],
            Q4=user_selected_answers['type_and_size'],
            Q5=user_selected_answers['preference_on_recycling_materials']
        )

        report = ReportGenerator(survey=survey)
        report_text = report.generate()

        ReportModel.objects.create(text=report_text)

        response_data = {'report_text': report_text}

        return JsonResponse(response_data, status=200)
    else:
        return JsonResponse({'error': 'Invalid data provided.'}, status=400)
