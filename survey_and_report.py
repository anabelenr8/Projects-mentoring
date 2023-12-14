from typing import Dict, Union, List

from survey_report.answers import Answers
from survey_report.report import Report, Survey

Answer = Union[str, List[str], Dict[str, Union[int, str]]]


def main_function():
    predetermined_answers: Dict[str, Answer] = {
        'Q1': Answers.CASUAL_AND_COMFORTABLE,
        'Q2': Answers.BRIGHT_AND_VIBRANT,
        'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
        'Q4': {'size': 14, 'type': Answers.TYPE_US},
        'Q5': {'answer': Answers.YES, 'choices': [Answers.CHOICE_ORGANIC,
                                                  Answers.CHOICE_RECYCLING]}
    }

    report = Report(survey=Survey(**predetermined_answers))
    report_text = report.generate()

    print('GENERATED REPORT:')
    print(report_text)


if __name__ == "__main__":
    main_function()
