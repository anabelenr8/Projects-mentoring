from django.test import TestCase
from rest_framework.response import Response
from rest_framework.test import APIClient


class TestSurveyReport(TestCase):

    def test_survey_and_answers(self):
        # Define API Client
        # (For tests, you can think of this as a requests package)
        client: APIClient = APIClient()

        # Create a GET request to your project's endpoint
        # Use Django REST Framework's Response as the type, not JsonResponse
        res: Response = client.get(
            '/api/survey',
        )
        self.assertEqual(
            res.status_code,
            200
        )
        self.assertEqual(
            res.json(),
            {
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
