import unittest

from survey_report.answers import Answers
from survey_report.report import Report, Survey


class TestReportGeneration(unittest.TestCase):
    def test_how_do_you_define_your_style(self):
        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.BRIGHT_AND_VIBRANT,
                        Q3=[Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES], Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Lorem ipsum 1. Question - ANSWER_1 dolor sit amet, consectetur adipiscing elit...'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.ELEGANT_AND_CHIC, Q2=Answers.BRIGHT_AND_VIBRANT,
                        Q3=[Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES], Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Lorem ipsum 1. Question - ANSWER_2 dolor sit amet, consectetur adipiscing elit...'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.BOHEMIAN_AND_RELAXED, Q2=Answers.BRIGHT_AND_VIBRANT,
                        Q3=[Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES], Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Sed vel bibendum tortor. Proin a aliquet tortor...'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.EDGY_AND_EXPERIMENTAL, Q2=Answers.BRIGHT_AND_VIBRANT,
                        Q3=[Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES], Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Mauris urna nunc, eleifend id sapien eget, tincidunt venenatis risus...'
        self.assertIn(expected_text, report_text)

    def test_describe_your_colour_pallette(self):
        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.BRIGHT_AND_VIBRANT,
                        Q3=[Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES], Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Mauris urna nunc, eleifend id sapien eget, 2. ' \
                        'Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus...'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.NEUTRAL_AND_SUBDUED,
                        Q3=[Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES], Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'In nisl ligula, porttitor vel lobortis vel, commodo quis mi...'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.DARK_AND_MUTED,
                        Q3=[Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES], Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1' \
                        ' or ANSWER_3 tincidunt venenatis risus...'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.PASTEL_AND_SOFT,
                        Q3=[Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES], Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'In nisl ligula, porttitor vel lobortis vel, commodo quis mi...'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.NO_ATTENTION,
                        Q3=[Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES], Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ' \
                        'ANSWER_3 tincidunt venenatis risus...'
        self.assertIn(expected_text, report_text)

    def test_shopping_category(self):
        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.NO_ATTENTION,
                        Q3=[Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES],
                        Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sollicitudin leo in 3.' \
                        ' Question - ANSWER_4, ANSWER_3 and ANSWER_1 lectus cursus tincidunt. ' \
                        'Nullam dapibus tincidunt libero nec volutpat.'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.NO_ATTENTION,
                        Q3=[Answers.BOTTOMS, Answers.SHOES], Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' \
                        ' Vestibulum dictum, dui non auctor tristique, odio sem 3. ' \
                        'Question - ANSWER_2 and ANSWER_5 convallis lacus, non gravida ' \
                        'libero erat id justo. Praesent in varius nisi. ' \
                        'Phasellus suscipit elit sit amet aliquam tincidunt.'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.NO_ATTENTION,
                        Q3=[Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES],
                        Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': Answers.CHOICE_ORGANIC})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
                        'Cras viverra luctus nunc, non ultrices mauris molestie vitae. ' \
                        'Sed gravida purus finibus 3. Question - ANSWER_4, ANSWER_3 or ANSWER_1 efficitur congue. ' \
                        'Vestibulum magna urna, volutpat vitae auctor non, pharetra vel leo.'

        self.assertIn(expected_text, report_text)

    def test_size_and_type(self):
        survey = Survey(Q4={'type': Answers.TYPE_EU})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'EU'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q4={'type': Answers.TYPE_UK})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'UK'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q4={'type': Answers.TYPE_US})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'US'
        self.assertIn(expected_text, report_text)

    def test_preference_on_recycling_material(self):
        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.NO_ATTENTION,
                        Q3=[Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES],
                        Q4={Answers.TYPE_US, 14}, Q5={'answer': Answers.NO})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Nam maximus et massa laoreet congue. In facilisis egestas neque. Nullam ac euismod nibh.' \
                        'ANSWER_NO Aenean pulvinar lacinia ligula, nec lobortis magna accumsan sed.'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.NO_ATTENTION,
                        Q3=[Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES],
                        Q4={Answers.TYPE_US, 14}, Q5={'answer': Answers.DONT_KNOW})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Phasellus ac sem ornare, ANSWER_I_DONT_KNOW euismod tellus id, sagittis felis. ' \
                        'Nullam viverra est nibh, et dignissim elit tincidunt nec. Integer vel dolor aliquam, ' \
                        'eleifend metus in, tincidunt erat. Nam id facilisis tortor.'
        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.NO_ATTENTION,
                        Q3=[Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES],
                        Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': [Answers.CHOICE_ORGANIC, Answers.CHOICE_RECYCLING]})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Mauris viverra lobortis ante, eget faucibus felis pulvinar et. Suspendisse urna diam,' \
                        ' ANSWER_YES and ANSWER_YES_CHOICE_2, ANSWER_YES_CHOICE_3 elementum nec tincidunt ornare, ' \
                        'convallis condimentum nisi.'

        self.assertIn(expected_text, report_text)

        survey = Survey(Q1=Answers.CASUAL_AND_COMFORTABLE, Q2=Answers.NO_ATTENTION,
                        Q3=[Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES],
                        Q4={Answers.TYPE_US, 14},
                        Q5={'answer': Answers.YES, 'choices': [Answers.CHOICE_WATER, Answers.CHOICE_NOT_SURE]})
        report = Report(survey=survey)
        report_text = report.generate()
        expected_text = 'Fusce sem est, maximus ac efficitur in, accumsan eu libero...'
        self.assertIn(expected_text, report_text)

    def assert_report_for_answer(self, predetermined_answers, expected_report_text):
        survey = Survey(**predetermined_answers)
        report = Report(survey=survey)
        report_text = report.generate()
        self.assertEqual(report_text, expected_report_text)


if __name__ == '__main__':
    unittest.main()
