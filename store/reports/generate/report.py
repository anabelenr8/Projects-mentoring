from store.reports.generate.answers import Answers
from store.reports.generate.survey import Survey


class Texts:
    CASUAL_AND_COMFORTABLE = (
        'Lorem ipsum 1. Question - '
        'ANSWER_1 dolor sit amet, consectetur adipiscing elit...'
    )

    ELEGANT_AND_CHIC = (
        'Lorem ipsum 1. Question - '
        'ANSWER_2 dolor sit amet, consectetur adipiscing elit...'
    )

    BOHEMIAN_AND_RELAXED = (
        'Sed vel bibendum tortor. Proin a aliquet tortor...'
    )
    EDGY_AND_EXPERIMENTAL = (
        'Mauris urna nunc, eleifend id sapien eget, '
        'tincidunt venenatis risus...'
    )

    BRIGHT_AND_VIBRANT = (
        'Mauris urna nunc, eleifend id sapien eget, 2.'
        'Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus...'
    )
    NEUTRAL_AND_SUBDUED = (
        'In nisl ligula, porttitor vel lobortis vel, commodo quis mi...'
    )

    DARK_AND_MUTED = (
        'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1'
        'or ANSWER_3 tincidunt venenatis risus...'
    )

    PASTEL_AND_SOFT = (
        'In nisl ligula, porttitor vel lobortis vel, commodo quis mi...'
    )

    NO_ATTENTION = (
        'Mauris urna nunc, eleifend id sapien eget, 2. '
        'Question - ANSWER_1 or '
        'ANSWER_3 tincidunt venenatis risus...'
    )

    TOPS_DRESSES_ACCESSORIES = (
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
        'Sed sollicitudin leo in 3.'
        ' Question - ANSWER_4, ANSWER_3 and ANSWER_1 '
        'lectus cursus tincidunt. '
        'Nullam dapibus tincidunt libero nec volutpat.'
    )
    BOTTOMS_SHOES = (
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
        ' Vestibulum dictum, dui non auctor tristique, odio sem 3. '
        'Question - ANSWER_2 and ANSWER_5 convallis lacus, non gravida '
        'libero erat id justo. Praesent in varius nisi. '
        'Phasellus suscipit elit sit amet aliquam tincidunt.'
    )
    TOPS_OR_DRESSES_OR_ACCESSORIES = (
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
        'Cras viverra luctus nunc, non ultrices mauris molestie vitae.'
        ' Sed gravida purus finibus '
        '3. Question - ANSWER_4, ANSWER_3 or ANSWER_1 efficitur congue.'
        ' Vestibulum magna urna, volutpat vitae auctor non, pharetra vel leo.'
    )
    ANSWER_NO = (
        'Nam maximus et massa laoreet congue.'
        'In facilisis egestas neque.Nullam ac euismod nibh.'
        'ANSWER_NO Aenean pulvinar lacinia ligula, nec lobortis '
        'magna accumsan sed.'
    )
    DONT_KNOW = (
        'Consectetur adipiscing elit, Phasellus ac sem ornare,'
        'ANSWER_I_DONT_KNOW euismod tellus id, sagittis felis.Nullam viverra'
        ' est nibh, et dignissim elit tincidunt nec.Integer vel dolor aliquam,'
        ' eleifend metus in, tincidunt erat.Nam id facilisis tortor.'
    )
    ORGANIC_AND_RECYCLING = (
        'Mauris viverra lobortis ante, eget faucibus felis pulvinar et. '
        'Suspendisse urna diam,'
        ' ANSWER_YES and ANSWER_YES_CHOICE_2, '
        'ANSWER_YES_CHOICE_3 elementum nec tincidunt ornare, '
        'convallis condimentum nisi.'

    )
    CHOICE_WATER_AND_NOT_SURE = (
        'Fusce sem est, maximus ac efficitur in,'
        ' accumsan eu libero...'

    )


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

        q1_answer = self.survey.Q1
        if q1_answer is not None:
            self.text += texts.get(q1_answer, "")

    def describe_your_color_palette(self):

        texts = {
            Answers.BRIGHT_AND_VIBRANT: Texts.BRIGHT_AND_VIBRANT,
            Answers.NEUTRAL_AND_SUBDUED: Texts.NEUTRAL_AND_SUBDUED,
            Answers.DARK_AND_MUTED: Texts.DARK_AND_MUTED,
            Answers.PASTEL_AND_SOFT: Texts.PASTEL_AND_SOFT,
            Answers.NO_ATTENTION: Texts.NO_ATTENTION
        }

        q2_answer = self.survey.Q2
        if q2_answer is not None:
            self.text += texts.get(q2_answer, "")

    def shopping_category(self):
        q3_answers = self.survey.Q3
        if q3_answers is not None:
            if set(self.survey.Q3) == {Answers.TOPS,
                                       Answers.DRESSES_AND_JUMPSUITS,
                                       Answers.ACCESSORIES}:

                self.text += Texts.TOPS_DRESSES_ACCESSORIES

            elif set(self.survey.Q3) == {Answers.BOTTOMS, Answers.SHOES}:

                self.text += Texts.BOTTOMS_SHOES

            if set(self.survey.Q3) & {Answers.TOPS,
                                      Answers.DRESSES_AND_JUMPSUITS,
                                      Answers.ACCESSORIES}:

                self.text += Texts.TOPS_OR_DRESSES_OR_ACCESSORIES

            else:
                self.text += 'Consectetur adipiscing elit,'
                'sed do eiusmod tempor'
                ' incididunt ut labore et'
                ' dolore magna aliqua...'

    def size_and_type(self):
        q4_data = self.survey.Q4
        if q4_data is not None:
            if 'type' in q4_data and q4_data['type'] == Answers.TYPE_EU:
                self.text += f" Your type is {Answers.TYPE_EU}"

            elif 'type' in q4_data and q4_data['type'] == Answers.TYPE_UK:
                self.text += f" Your type is {Answers.TYPE_UK}"

            elif 'type' in q4_data and q4_data['type'] == Answers.TYPE_US:
                self.text += f" Your type is {Answers.TYPE_US}"

            if 'size' in q4_data:
                clothe_size = q4_data['size']
                self.text += (
                    f"Your clothing size is"
                    f" {q4_data['size']} "
                    f"{self.calculate_recommendation(size=clothe_size)}"
                )

    def preference_on_recycling_material(self):
        q5_data = self.survey.Q5
        if q5_data and isinstance(q5_data, dict) and 'answer' in q5_data:
            if q5_data['answer'] == Answers.NO:
                self.text += Texts.ANSWER_NO

            elif q5_data['answer'] == Answers.DONT_KNOW:
                self.text += Texts.DONT_KNOW

            elif q5_data['answer'] == Answers.YES and 'choices' in q5_data:
                choices = q5_data['choices']

                if (
                        Answers.CHOICE_ORGANIC in choices and
                        Answers.CHOICE_RECYCLING in choices
                ):
                    self.text += Texts.ORGANIC_AND_RECYCLING

                elif (
                        Answers.CHOICE_WATER in choices and
                        Answers.CHOICE_NOT_SURE in choices
                ):
                    self.text += Texts.CHOICE_WATER_AND_NOT_SURE
            else:
                self.text += 'Lorem ipsum dolor sit amet, ' + \
                             'consectetur adipiscing elit.' \
                             ' Pellentesque sed scelerisque' + \
                             ' nulla, at mattis mauris.' \
                             ' Vestibulum dignissim viverra' + \
                             ' nulla quis tempus. (Any other case)'

    def generate(self) -> str:
        self.how_you_define_your_style()
        self.describe_your_color_palette()
        self.shopping_category()
        self.size_and_type()
        self.preference_on_recycling_material()

        return self.text
