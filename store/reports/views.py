import json

from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods

from store.serializers import UserAnswersSerializer


@require_http_methods(['GET'])
def get_api_survey_and_answers(request: HttpRequest) -> JsonResponse:
    print(request)
    return JsonResponse(
        status=200,
        data={
            'How do you define your style?': [
                'casual and comfortable',
                'elegant and chic',
                'bohemian and relaxed',
                'edgy and experimental',
                'none of the above'
            ],
            'Describe your colour palette?': [
                'bright and vibrant',
                'neutral and subdued',
                'dark and muted',
                'pastel and soft',
                'I don\'t pay much attention to colors'
            ],
            'What is your shopping category?': [
                'Tops',
                'Bottoms',
                'Dresses and Jumpsuits',
                'Accessories',
                'Shoes',
            ],
            'What is your type and size of measurements?': [
                'Type UK',
                'Type US',
                'Type EU',
            ],
            'What is your preference on recycling materials?': [
                'Organic Materials',
                'Recycling Materials',
                'Reuse of Water',
                'Not Sure',
            ]
        }
    )


@require_http_methods(['POST'])
def post_report_generation(request):
    try:
        request_data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    required_fields = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
    missing_fields = [field for field in required_fields if field not in request_data]
    if missing_fields:
        return JsonResponse(
            {'error': f"Missing answers for: {', '.join(missing_fields)}."},
            status=400
        )

    serializer = UserAnswersSerializer(data=request_data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        # Format list values as comma-separated strings
        q3_answer_formatted = ', '.join(validated_data['Q3'])
        q4_answer_formatted = ', '.join(validated_data['Q4'])

        response_data = {
            'user choice': validated_data,
            'Generated Report':
                f'Lorem ipsum 1. Question - {validated_data["Q1"]} dolor sit amet, consectetur adipiscing '
                f'elit...Mauris urna nunc, eleifend id sapien eget, 2.Question - {validated_data["Q2"]} or '
                f'{q3_answer_formatted} tincidunt venenatis risus...Lorem ipsum dolor sit amet, consectetur '
                f'adipiscing elit. Cras viverra luctus nunc, non ultrices mauris molestie vitae. '
                f'Sed gravida purus finibus 3. Question - {q4_answer_formatted}, {validated_data["Q5"]["answer"]} or '
                f'{validated_data["Q5"]["choices"]} efficitur congue. Vestibulum magna urna, volutpat vitae '
                f'auctor non, pharetra vel leo. Your type is USYour clothing size is 14 Your clothing '
                f'size is suitable.Mauris viverra lobortis ante, eget faucibus felis pulvinar et. '
                f'Suspendisse urna diam, elementum nec tincidunt ornare, convallis condimentum nisi.'
        }

        return JsonResponse(response_data, status=200)
    else:
        return JsonResponse({'error': 'You must answer all questions.'}, status=400)
