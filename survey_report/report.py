from survey_report.answers import Answers
from survey_report.survey import Survey


class Texts:
    CASUAL_AND_COMFORTABLE = 'Lorem ipsum 1. Question - ANSWER_1 dolor sit amet, consectetur adipiscing elit...'
    ELEGANT_AND_CHIC = 'Lorem ipsum 1. Question - ANSWER_2 dolor sit amet, consectetur adipiscing elit...'
    BOHEMIAN_AND_RELAXED = 'Sed vel bibendum tortor. Proin a aliquet tortor...'
    EDGY_AND_EXPERIMENTAL = 'Mauris urna nunc, eleifend id sapien eget, tincidunt venenatis risus...'

    BRIGHT_AND_VIBRANT = 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus...'
    NEUTRAL_AND_SUBDUED = 'In nisl ligula, porttitor vel lobortis vel, commodo quis mi...'
    DARK_AND_MUTED = 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus...'
    PASTEL_AND_SOFT = 'In nisl ligula, porttitor vel lobortis vel, commodo quis mi...'
    NO_ATTENTION = 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus...'


class Report:
    def __init__(self, survey: Survey):
        self.survey = survey
        self.text = ''

    def calculate_recommendation(self, size: int) -> str:
        if size > 16:
            return "Consider choosing larger-sized clothing for comfort."
        else:
            return "Your clothing size is suitable."

    def how_you_define_your_style(self):

        texts = {
            Answers.CASUAL_AND_COMFORTABLE: Texts.CASUAL_AND_COMFORTABLE,
            Answers.ELEGANT_AND_CHIC: Texts.ELEGANT_AND_CHIC,
            Answers.BOHEMIAN_AND_RELAXED: Texts.BOHEMIAN_AND_RELAXED,
            Answers.EDGY_AND_EXPERIMENTAL: Texts.EDGY_AND_EXPERIMENTAL
        }

        self.text += texts[self.survey.Q1]

    def describe_your_color_palette(self):

        texts = {
            Answers.BRIGHT_AND_VIBRANT: Texts.BRIGHT_AND_VIBRANT,
            Answers.NEUTRAL_AND_SUBDUED: Texts.NEUTRAL_AND_SUBDUED,
            Answers.DARK_AND_MUTED: Texts.DARK_AND_MUTED,
            Answers.PASTEL_AND_SOFT: Texts.PASTEL_AND_SOFT,
            Answers.NO_ATTENTION: Texts.NO_ATTENTION
        }

        self.text += texts[self.survey.Q2]

    def shopping_category(self):
        if set(self.survey.Q3) == {Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES}:
            self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sollicitudin leo in 3. Question - ANSWER_4, ANSWER_3 and ANSWER_1 lectus cursus tincidunt...'
        elif set(self.survey.Q3) == {Answers.BOTTOMS, Answers.SHOES}:
            self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum dictum, dui non auctor tristique, odio sem 3. Question - ANSWER_2 and ANSWER_5 convallis lacus...'
        if set(self.survey.Q3) & {Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES}:
            self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra luctus nunc, non ultrices mauris molestie vitae...'
        else:
            self.text += 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua...'

    def size_and_type(self):
        if self.survey.Q4['type'] == Answers.TYPE_EU:
            self.text += f" Your type is {Answers.TYPE_EU}"
        elif self.survey.Q4['type'] == Answers.TYPE_UK:
            self.text += f" Your type is {Answers.TYPE_UK}"
        if self.survey.Q4['type'] == Answers.TYPE_US:
            self.text += f" Your type is {Answers.TYPE_US}"
            clothe_size = self.survey.Q4['size']
            self.text += f"Your clothing size is {self.survey.Q4['size']} {self.calculate_recommendation(size=clothe_size)}"

    def preference_on_recycling_material(self):
        if self.survey.Q5['answer'] == Answers.NO:
            self.text += 'Nam maximus et massa laoreet congue...'
        elif self.survey.Q5['answer'] == Answers.DONT_KNOW:
            self.text += 'Phasellus ac sem ornare, ANSWER_I_DONT_KNOW euismod tellus id, sagittis felis...'
        if (
                self.survey.Q5['answer'] == Answers.YES
                and {Answers.CHOICE_ORGANIC, Answers.CHOICE_RECYCLING
                     }.issubset(self.survey.Q5['choices'])
        ):
            self.text += 'Mauris viverra lobortis ante, eget faucibus felis pulvinar et...'
        if self.survey.Q5['answer'] == Answers.YES and {Answers.CHOICE_WATER, Answers.CHOICE_NOT_SURE}.issubset(
                self.survey.Q5):
            self.text += 'Fusce sem est, maximus ac efficitur in, accumsan eu libero...'
        else:
            self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...'

    def generate(self) -> str:
        self.how_you_define_your_style()
        self.describe_your_color_palette()
        self.shopping_category()
        self.size_and_type()
        self.preference_on_recycling_material()

        return self.text
