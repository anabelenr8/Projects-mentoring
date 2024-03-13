from django.test import TestCase
from rest_framework.test import APIClient


class TestSurveyReport(TestCase):
    def test_survey_and_answers(self):
        client = APIClient()

        res = client.get('/api/survey/')

        self.assertEqual(
            res.status_code,
            200
        )

        expected_data = {
            "How do you define your style?": [
                "casual and comfortable",
                "elegant and chic",
                "bohemian and relaxed",
                "edgy and experimental",
                "none of the above"
            ],
            "Describe your colour palette?": [
                "bright and vibrant",
                "neutral and subdued",
                "dark and muted",
                "pastel and soft",
                "I don't pay much attention to colors"
            ],
            "What is your shopping category?": [
                "Tops",
                "Bottoms",
                "Dresses and Jumpsuits",
                "Accessories",
                "Shoes"
            ],
            "What is your type and size of measurements?": [
                "Type UK",
                "Type US",
                "Type EU"
            ],
            "What is your preference on recycling materials?": [
                "Organic Materials",
                "Recycling Materials",
                "Reuse of Water",
                "Not Sure"
            ]
        }

        self.assertDictEqual(
            res.json(),
            expected_data
        )


class TestSurveyReportPost(TestCase):
    def test_how_you_define_your_style(self):
        client = APIClient()

        request_data = {
            'Q1': 'casual and comfortable',
            'Q2': 'bright and vibrant',
            'Q3': ['tops', 'bottoms', 'accessories'],
            'Q4': ['US'],
            'Q5': {
                'answer': 'yes',
                'choices': 'use organic materials'
            }
        }

        expected_generated_report = (
            "Lorem ipsum 1. Question - casual and comfortable dolor sit amet, consectetur adipiscing "
            "elit...Mauris urna nunc, eleifend id sapien eget, 2.Question - bright and vibrant or "
            "tops, bottoms, accessories tincidunt venenatis risus...Lorem ipsum dolor sit amet, consectetur "
            "adipiscing elit. Cras viverra luctus nunc, non ultrices mauris molestie vitae. "
            "Sed gravida purus finibus 3. Question - US, yes or use organic materials efficitur "
            "congue. Vestibulum magna urna, volutpat vitae auctor non, pharetra vel leo. Your "
            "type is USYour clothing size is 14 Your clothing size is suitable.Mauris viverra "
            "lobortis ante, eget faucibus felis pulvinar et. Suspendisse urna diam, elementum nec tincidunt "
            "ornare, convallis condimentum nisi."
        )

        res = client.post \
            ('/api/report/',
             data=request_data,
             format='json'
             )

        self.assertEqual(
            res.status_code,
            200
        )

        self.assertEqual(
            res.json()['Generated Report'],
            expected_generated_report
        )

    def test_incomplete_user_answers(self):
        client = APIClient()

        incomplete_request_data = {
            'Q1': 'casual and comfortable',
            # Q2 is omitted to simulate a missing answer
            'Q3': ['tops', 'bottoms', 'accessories'],
            'Q4': ['US'],
            # Q5 is omitted to simulate a missing answer
        }

        expected_error_message = "Missing answers for: Q2, Q5."

        res = client.post(
            '/api/report/',
            data=incomplete_request_data,
            format='json'
        )

        self.assertEqual(
            res.status_code,
            400
        )

        self.assertEqual(
            res.json().get('error'),
            expected_error_message
        )
