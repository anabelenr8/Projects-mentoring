import json

from django.http.request import HttpRequest
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.reports.docs import post_report_description
from store.reports.docs.get_survey_description import get_report_description
from store.reports.generate.report import Report as ReportGenerator
from store.reports.generate.survey import Survey
from store.reports.models import Report as ReportModel
from store.reports.serializers import SurveySerializer


class QuestionSerializer(serializers.Serializer):
    key = serializers.CharField()
    display_name = serializers.CharField()


class AnswerSerializer(serializers.Serializer):
    key = serializers.CharField()
    display_name = serializers.CharField()


class SurveyQuestionSerializer(serializers.Serializer):
    question = QuestionSerializer()
    answers = AnswerSerializer(many=True)


@swagger_auto_schema(
    method='GET',
    tags=["Survey"],
    operation_description=get_report_description,
    operation_summary='Retrieves Questions and possible Answers',
    operation_id='get_survey_questions',
    responses={200: SurveyQuestionSerializer(many=True)}
)
@api_view(['GET'])
def get_api_survey_and_answers(request: HttpRequest) -> Response:
    data = [
        {
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

                {'key': 'none_above',
                 'display_name': 'None of the above'},
            ],
        },
        {
            'question': {
                'key': 'colour_palette',
                'display_name': 'Describe your colour palette?',
            },
            'answers': [
                {'key': 'bright_vibrant',
                 'display_name': 'Bright and Vibrant'},

                {'key': 'neutral_subdued',
                 'display_name': 'Neutral and Subdued'},

                {'key': 'dark_muted',
                 'display_name': 'Dark and Muted'},

                {'key': 'pastel_soft',
                 'display_name': 'Pastel and Soft'},

                {'key': 'not_attention_colors',
                 'display_name': "I don't pay much attention to colors"},
            ],
        },
        {
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
        {
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
        {
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

                {'key': 'reuse_water',
                 'display_name': 'Reuse of Water'},

                {'key': 'not_sure', 'display_name': 'Not Sure'},
            ],
        },
    ]
    serializer = SurveyQuestionSerializer(data=data, many=True)
    serializer.is_valid(raise_exception=True)

    return Response(
        status=200,
        data=serializer.data
    )


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportModel
        fields = [
            'uid',
            'text',
        ]


example_request_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'your_style': openapi.Schema(type=openapi.TYPE_STRING,
                                     example="casual_and_comfortable"),
        'colour_palette': openapi.Schema(type=openapi.TYPE_STRING,
                                         example="bright_and_vibrant"),
        'shopping_category': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING),
            example=["tops", "bottoms", "accessories"]
        ),
        'type_and_size': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'size': openapi.Schema(type=openapi.TYPE_INTEGER, example=14),
                'type': openapi.Schema(type=openapi.TYPE_STRING,
                                       example="type_us")
            }
        ),
        'preference_on_recycling_materials': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'answer': openapi.Schema(type=openapi.TYPE_STRING,
                                         example="yes"),
                'choices': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_STRING),
                    example=["use_organic_materials", "recycling_initiatives"]
                )
            }
        )
    },
    required=['your_style', 'colour_palette', 'shopping_category',
              'type_and_size', 'preference_on_recycling_materials']
)


@swagger_auto_schema(
    method='POST',
    operation_description=post_report_description,
    operation_id='post_report',
    request_body=example_request_body,
    operation_summary='Create a Report by submitting Survey Answers',
    tags=["Report"],
    responses={200: ReportSerializer()},

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

    report_text = ReportGenerator(survey=survey).generate()

    report = ReportModel.objects.create(text=report_text)

    return Response(
        data=ReportSerializer(instance=report).data,
        status=200
    )
