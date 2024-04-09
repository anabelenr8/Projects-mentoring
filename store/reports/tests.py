import copy

from django.test import TestCase
from rest_framework.test import APIClient

from store.reports.generate.answers import Answers
from store.reports.generate.report import Report, Survey


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

                    {'key': 'dark_muted',
                     'display_name': 'Dark and Muted'},

                    {'key': 'pastel_soft',
                     'display_name': 'Pastel and Soft'},

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
                    {'key': 'tops',
                     'display_name': 'Tops'},

                    {'key': 'bottoms',
                     'display_name': 'Bottoms'},

                    {'key': 'dresses_jumpsuits',
                     'display_name': 'Dresses and Jumpsuits'},

                    {'key': 'accessories',
                     'display_name': 'Accessories'},

                    {'key': 'shoes',
                     'display_name': 'Shoes'},
                ],
            },
            'type_and_size': {
                'question': {
                    'key': 'type_and_size',
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
                'choices': ['use_organic_materials', 'recycling_initiatives']

            }
        }

        expected_generated_report = (
            'Lorem ipsum 1. Question - ANSWER_1 dolor sit amet, consectetur'
            ' adipiscing elit...Mauris urna nunc, eleifend id sapien eget,'
            ' 2.Question - ANSWER_1 or ANSWER_3 tincidunt venenatis '
            'risus...Lorem ipsum dolor sit amet, consectetur adipiscing'
            ' elit. Cras viverra luctus nunc, non ultrices mauris molestie'
            ' vitae. Sed gravida purus finibus 3. Question - '
            'ANSWER_4, ANSWER_3 or ANSWER_1 efficitur congue. '
            'Vestibulum magna urna, volutpat vitae auctor non, '
            'pharetra vel leo. Your type is type_usYour '
            'clothing size is 14 Your clothing size is suitable.'
            'Mauris viverra lobortis ante, eget faucibus felis '
            'pulvinar et. Suspendisse urna diam, ANSWER_YES and '
            'ANSWER_YES_CHOICE_2, ANSWER_YES_CHOICE_3 elementum '
            'nec tincidunt ornare, convallis condimentum nisi.'
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


class TestReportGeneration(TestCase):
    test_data = {
        'predetermined_answers': {
            'Q1': Answers.CASUAL_AND_COMFORTABLE,
            'Q2': Answers.BRIGHT_AND_VIBRANT,
            'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
            'Q4': {Answers.TYPE_US, 14},
            'Q5': {
                'answer': Answers.YES,
                'choices': Answers.CHOICE_ORGANIC
            }
        }
    }

    def test_how_do_you_define_your_style(self):
        test_cases = [
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.BRIGHT_AND_VIBRANT,
                    'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'Lorem ipsum 1. Question - '
                    'ANSWER_1 dolor sit amet, consectetur adipiscing elit...'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.ELEGANT_AND_CHIC,
                    'Q2': Answers.BRIGHT_AND_VIBRANT,
                    'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'Lorem ipsum 1. Question - '
                    'ANSWER_2 dolor sit amet, consectetur adipiscing elit...'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.BOHEMIAN_AND_RELAXED,
                    'Q2': Answers.BRIGHT_AND_VIBRANT,
                    'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'Sed vel bibendum tortor. Proin a aliquet tortor...'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.EDGY_AND_EXPERIMENTAL,
                    'Q2': Answers.BRIGHT_AND_VIBRANT,
                    'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'Mauris urna nunc, eleifend id sapien eget, '
                    'tincidunt venenatis risus...'
                ),
            },
        ]

        for test_case in test_cases:
            report = Report(
                survey=Survey(**test_case['predetermined_answers'])
            )
            self.assertIn(
                test_case['expected_text'],
                report.generate()
            )

    def test_describe_your_colour_palette(self):
        test_cases = [

            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.BRIGHT_AND_VIBRANT,
                    'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'Mauris urna nunc, eleifend id sapien eget, 2.'
                    'Question - ANSWER_1 or ANSWER_3 '
                    'tincidunt venenatis risus...'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.NEUTRAL_AND_SUBDUED,
                    'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'In nisl ligula, porttitor vel lobortis vel, '
                    'commodo quis mi...'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.DARK_AND_MUTED,
                    'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'Mauris urna nunc, eleifend id sapien eget,'
                    ' 2. Question - ANSWER_1'
                    'or ANSWER_3 tincidunt venenatis risus...'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.PASTEL_AND_SOFT,
                    'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'In nisl ligula, porttitor vel lobortis vel,'
                    ' commodo quis mi...'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.NO_ATTENTION,
                    'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'Mauris urna nunc, eleifend id sapien eget, 2. '
                    'Question - ANSWER_1 or '
                    'ANSWER_3 tincidunt venenatis risus...'
                ),
            },
        ]

        for test_case in test_cases:
            report = Report(
                survey=Survey(**test_case['predetermined_answers'])
            )
            self.assertIn(
                test_case['expected_text'],
                report.generate()
            )

    def test_shopping_category(self):

        test_cases = [
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.BRIGHT_AND_VIBRANT,
                    'Q3': [Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS,
                           Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                    'Sed sollicitudin leo in 3.'
                    ' Question - ANSWER_4, ANSWER_3 and ANSWER_1 '
                    'lectus cursus tincidunt. '
                    'Nullam dapibus tincidunt libero nec volutpat.'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.NEUTRAL_AND_SUBDUED,
                    'Q3': [Answers.BOTTOMS, Answers.SHOES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
                    ' Vestibulum dictum, dui non auctor '
                    'tristique, odio sem 3. '
                    'Question - ANSWER_2 and ANSWER_5 '
                    'convallis lacus, non gravida '
                    'libero erat id justo. Praesent in varius nisi. '
                    'Phasellus suscipit elit sit amet aliquam tincidunt.'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.DARK_AND_MUTED,
                    'Q3': [Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS,
                           Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': Answers.CHOICE_ORGANIC
                    }
                },
                'expected_text': (
                    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                    'Cras viverra luctus nunc, non'
                    ' ultrices mauris molestie vitae.'
                    ' Sed gravida purus finibus '
                    '3. Question - ANSWER_4, ANSWER_3'
                    ' or ANSWER_1 efficitur congue.'
                    ' Vestibulum magna urna, volutpat '
                    'vitae auctor non, pharetra vel leo.'
                ),
            },

        ]
        for test_case in test_cases:
            report = Report(
                survey=Survey(**test_case['predetermined_answers'])
            )
            self.assertIn(
                test_case['expected_text'],
                report.generate()
            )

    def test_size_and_type(self):

        test_data = copy.deepcopy(self.test_data)

        predetermined_answers = test_data['predetermined_answers']

        test_cases = [
            {
                'predetermined_answers': {
                    'Q4': {'type': Answers.TYPE_UK}
                },

                'expected_text': 'type_uk'
            },
            {
                'predetermined_answers': {
                    'Q4': {'type': Answers.TYPE_EU}
                },

                'expected_text': 'type_eu'
            },

            {
                'predetermined_answers': {
                    'Q4': {'type': Answers.TYPE_US}
                },

                'expected_text': 'type_us'
            }
        ]
        for test_case in test_cases:
            predetermined_answers.update(test_case['predetermined_answers'])

            report = Report(survey=Survey(**predetermined_answers))

            self.assertIn(
                test_case['expected_text'],
                report.generate()
            )

    def test_preference_on_recycling_material(self):

        test_cases = [
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.BRIGHT_AND_VIBRANT,
                    'Q3': [Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS,
                           Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.NO

                    }
                },
                'expected_text': (
                    'Nam maximus et massa laoreet congue.'
                    'In facilisis egestas neque.Nullam ac euismod nibh.'
                    'ANSWER_NO Aenean pulvinar lacinia ligula, nec lobortis '
                    'magna accumsan sed.'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.NEUTRAL_AND_SUBDUED,
                    'Q3': [Answers.BOTTOMS, Answers.SHOES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.DONT_KNOW,

                    }
                },
                'expected_text': (
                    'Consectetur adipiscing elit,'
                    ' Phasellus ac sem ornare,'
                    'ANSWER_I_DONT_KNOW euismod tellus id, '
                    'sagittis felis.Nullam viverra'
                    ' est nibh, et dignissim elit tincidunt nec.'
                    'Integer vel dolor aliquam,'
                    ' eleifend metus in, tincidunt erat.Nam id '
                    'facilisis tortor.'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.DARK_AND_MUTED,
                    'Q3': [Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS,
                           Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': [Answers.CHOICE_ORGANIC,
                                    Answers.CHOICE_RECYCLING]
                    }
                },
                'expected_text': (
                    'Mauris viverra lobortis ante, eget faucibus felis'
                    ' pulvinar et. Suspendisse urna diam, ANSWER_YES and '
                    'ANSWER_YES_CHOICE_2, ANSWER_YES_CHOICE_3 elementum nec '
                    'tincidunt ornare, convallis condimentum nisi.'
                ),
            },
            {
                'predetermined_answers': {
                    'Q1': Answers.CASUAL_AND_COMFORTABLE,
                    'Q2': Answers.DARK_AND_MUTED,
                    'Q3': [Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS,
                           Answers.ACCESSORIES],
                    'Q4': {Answers.TYPE_US, 14},
                    'Q5': {
                        'answer': Answers.YES,
                        'choices': [Answers.CHOICE_WATER,
                                    Answers.CHOICE_NOT_SURE]
                    }
                },
                'expected_text': (
                    'Fusce sem est, maximus ac efficitur in, '
                    'accumsan eu libero...'
                ),
            }

        ]

        for test_case in test_cases:
            report = Report(
                survey=Survey(**test_case['predetermined_answers'])

            )

            self.assertIn(
                test_case['expected_text'],
                report.generate()

            )
