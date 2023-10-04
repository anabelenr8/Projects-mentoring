from survey_report.answers import Answers
from survey_report.report import Report, Survey


def main_function():
    # Predetermined answers
    predetermined_answers = {
        'Q1': Answers.ELEGANT_AND_CHIC,
        'Q2': Answers.PASTEL_AND_SOFT,
        'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
        'Q4': {'size': 14,
               'type': Answers.TYPE_UK},
        'Q5': Answers.NO
    }

    user_submitted_survey = Survey(**predetermined_answers)

    # Generate report based on survey answers
    report = Report(survey=user_submitted_survey)
    report_text = report.generate()  # Outputs report text which is generated based on survey answers

    # Iterate through the predetermined answers and print in the desired format
    for question, selected_answer in predetermined_answers.items():
        # Get the text associated with the selected answer
        answer_text = report_text
        # Print in the desired format
        print(f'{question} = {selected_answer}\n{answer_text}\n')


if __name__ == "__main__":
    main_function()
