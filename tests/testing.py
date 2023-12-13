import copy
import unittest

from survey_report.answers import Answers
from survey_report.report import Report, Survey


class TestReportGeneration(unittest.TestCase):
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

                'expected_text': 'UK'
            },
            {
                'predetermined_answers': {
                    'Q4': {'type': Answers.TYPE_EU}
                },

                'expected_text': 'EU'
            },

            {
                'predetermined_answers': {
                    'Q4': {'type': Answers.TYPE_US}
                },

                'expected_text': 'US'
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


if __name__ == '__main__':
    unittest.main()
