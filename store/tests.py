from django.test import TestCase
from rest_framework.test import APIClient


class TestSurveyReportGet(TestCase):
    def test_survey_and_answers(self):
        client = APIClient()

        res = client.get('/api/survey/')

        self.assertEqual(
            res.status_code,
            200
        )
        expected_data = {
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
        }

        self.assertDictEqual(
            res.json(),
            expected_data
        )


class TestSurveyReportPost(TestCase):
    def test_report_generation(self):
        client = APIClient()

        request_data = {
            'your_style': 'casual_and_comfortable',
            'colour_palette': 'bright_and_vibrant',
            'shopping_category': ['tops', 'bottoms', 'accessories'],
            'type_and_size': {
                'size': 14,
                'type': 'type_us',
            },
            'preference_on_recycling_materials': {
                'answer': 'yes',
                'choices': 'organic_materials'
            }
        }

        expected_generated_report = (
            'Lorem ipsum 1. Question - ANSWER_1 dolor sit amet,'
            ' consectetur adipiscing elit...Mauris urna nunc,'
            ' eleifend id sapien eget, 2.Question - ANSWER_1 or ANSWER_3'
            ' tincidunt venenatis risus...Lorem ipsum dolor sit amet,'
            ' consectetur adipiscing elit. Cras viverra luctus nunc,'
            ' non ultrices mauris molestie vitae. Sed gravida purus'
            ' finibus 3. Question - ANSWER_4, ANSWER_3 or ANSWER_1 '
            'efficitur congue. Vestibulum magna urna, volutpat vitae auctor'
            ' non, pharetra vel leo. Your type is type_us'
            'Your clothing size is 14 Your clothing size is suitable.'
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
            res.json()['report_text'],
            expected_generated_report
        )
