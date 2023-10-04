from survey_report.answers import Answers
from survey_report.survey import Survey


class Report:
    def __init__(self, survey: Survey):
        self.survey = survey
        self.text = ''

    def calculate_recommendation(self, size: int) -> str:
        if size > 16:
            return "Consider choosing larger-sized clothing for comfort."
        else:
            return "Your clothing size is suitable."

    def generate(self) -> str:

        if self.survey.Q1 == Answers.CASUAL_AND_COMFORTABLE:
            self.text += 'Lorem ipsum 1. Question - ANSWER_1 dolor sit amet, consectetur adipiscing elit...'
        elif self.survey.Q1 == Answers.ELEGANT_AND_CHIC:
            self.text += 'Lorem ipsum 1. Question - ANSWER_2 dolor sit amet, consectetur adipiscing elit...'
        elif self.survey.Q1 == Answers.BOHEMIAN_AND_RELAXED:
            self.text += 'Sed vel bibendum tortor. Proin a aliquet tortor...'
        elif self.survey.Q1 == Answers.EDGY_AND_EXPERIMENTAL or self.survey.Q1 == Answers.NONE_OF_THE_ABOVE:
            self.text += 'Mauris urna nunc, eleifend id sapien eget, tincidunt venenatis risus...'

            # Logic for generating the report text based on Q2 answer
        if self.survey.Q2 == Answers.BRIGHT_AND_VIBRANT:
            self.text += 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus...'
        elif self.survey.Q2 == Answers.NEUTRAL_AND_SUBDUED:
            self.text += 'In nisl ligula, porttitor vel lobortis vel, commodo quis mi...'
        elif self.survey.Q2 == Answers.DARK_AND_MUTED:
            self.text += 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus...'
        elif self.survey.Q2 == Answers.PASTEL_AND_SOFT:
            self.text += 'In nisl ligula, porttitor vel lobortis vel, commodo quis mi...'
        elif self.survey.Q2 == Answers.NO_ATTENTION:
            self.text += 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus...'

            # Logic for generating the report text based on Q3 answer
        if set(self.survey.Q3) == {Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES}:
            self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sollicitudin leo in 3. Question - ANSWER_4, ANSWER_3 and ANSWER_1 lectus cursus tincidunt...'
        elif set(self.survey.Q3) == {Answers.BOTTOMS, Answers.SHOES}:
            self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum dictum, dui non auctor tristique, odio sem 3. Question - ANSWER_2 and ANSWER_5 convallis lacus...'
        elif set(self.survey.Q3) & {Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES}:
            self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra luctus nunc, non ultrices mauris molestie vitae...'
        else:
            self.text += 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua...'

        # Logic for generating the report text based on Q4 answer
        if self.survey.Q4 == Answers.TYPE_EU:
            self.text += f" Your type is {Answers.TYPE_EU}"
        elif self.survey.Q4 == Answers.TYPE_UK:
            self.text += f" Your type is {Answers.TYPE_UK}"
        elif self.survey.Q4 == Answers.TYPE_US:
            self.text += f" Your type is {Answers.TYPE_US}"
            clothe_size = predetermined_answers['Q4']['size']
            clothe_recommendation = self.calculate_recommendation(size=clothe_size)
            self.text += f"Your clothing size is {self.calculate_recommendation(size=clothe_size)}. {clothe_recommendation}\n"

        # Logic for generating the report text based on Q5 answer
        if self.survey.Q5 == Answers.NO:
            self.text += 'Nam maximus et massa laoreet congue...'
        elif self.survey.Q5 == Answers.DONT_KNOW:
            self.text += 'Phasellus ac sem ornare, ANSWER_I_DONT_KNOW euismod tellus id, sagittis felis...'
        if self.survey.Q5 == Answers.YES and {2, 3}.issubset(self.survey.Q5):
            self.text += 'Mauris viverra lobortis ante, eget faucibus felis pulvinar et...'
        if self.survey.Q5 == Answers.YES and {1, 4}.issubset(self.survey.Q5):
            self.text += 'Fusce sem est, maximus ac efficitur in, accumsan eu libero...'
        else:
            self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...'

        return self.text
