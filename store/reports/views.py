from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods


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
