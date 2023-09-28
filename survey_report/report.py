from .survey import Survey, predetermined_answers, Answers


class Report:
    def __init__(self, survey: Survey):
        self.survey = survey
        self.text = ''

    def calculate_recommendation(self, size: 'Any') -> str:
        if size > 16:
            return "Consider choosing larger-sized clothing for comfort."
        else:
            return "Your clothing size is suitable."

    def generate(self) -> str:
        if 'Q1' in predetermined_answers:
            q1_answer = predetermined_answers['Q1']
            if q1_answer == Answers.CASUAL_AND_COMFORTABLE:
                self.text += 'Lorem ipsum 1. Question - ANSWER_1 dolor sit amet, consectetur adipiscing elit...'
            elif q1_answer == Answers.ELEGANT_AND_CHIC:
                self.text += 'Lorem ipsum 1. Question - ANSWER_2 dolor sit amet, consectetur adipiscing elit...'
            elif q1_answer == Answers.BOHEMIAN_AND_RELAXED:
                self.text += 'Sed vel bibendum tortor. Proin a aliquet tortor...'
            elif q1_answer == Answers.EDGY_AND_EXPERIMENTAL or q1_answer == Answers.NONE_OF_THE_ABOVE:
                self.text += 'Mauris urna nunc, eleifend id sapien eget, tincidunt venenatis risus...'

        # Logic for generating the report text based on Q2 answer
        if 'Q2' in predetermined_answers:
            q2_answer = predetermined_answers['Q2']
            if q2_answer == Answers.BRIGHT_AND_VIBRANT:
                self.text += 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus...'
            elif q2_answer == Answers.NEUTRAL_AND_SUBDUED:
                self.text += 'In nisl ligula, porttitor vel lobortis vel, commodo quis mi...'
            elif q2_answer == Answers.DARK_AND_MUTED:
                self.text += 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus...'
            elif q2_answer == Answers.PASTEL_AND_SOFT:
                self.text += 'In nisl ligula, porttitor vel lobortis vel, commodo quis mi...'
            elif q2_answer == Answers.NO_ATTENTION:
                self.text += 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus...'

        # Logic for generating the report text based on Q3 answer
        if 'Q3' in predetermined_answers:
            q3_answers = predetermined_answers['Q3']
            if set(q3_answers) == {Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES}:
                self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sollicitudin leo in 3. Question - ANSWER_4, ANSWER_3 and ANSWER_1 lectus cursus tincidunt...'
            elif set(q3_answers) == {Answers.BOTTOMS, Answers.SHOES}:
                self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum dictum, dui non auctor tristique, odio sem 3. Question - ANSWER_2 and ANSWER_5 convallis lacus...'
            elif set(q3_answers) & {Answers.TOPS, Answers.DRESSES_AND_JUMPSUITS, Answers.ACCESSORIES}:
                self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra luctus nunc, non ultrices mauris molestie vitae...'
            else:
                self.text += 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua...'

        # Logic for generating the report text based on Q4 answer
        if 'Q4' in predetermined_answers:
            q4_answer = predetermined_answers['Q4']
            if Answers.size in q4_answer:
                clothe_size = predetermined_answers['Q4'][Answers.size]
                recommendation = self.calculate_recommendation(clothe_size)
                self.text += f"Your clothing size is {clothe_size}. {recommendation}\n"

        # Logic for generating the report text based on Q5 answer
        if 'Q5' in predetermined_answers:
            q5_answer = predetermined_answers['Q5']
            if q5_answer == Answers.NO:
                self.text += 'Nam maximus et massa laoreet congue...'
            elif q5_answer == Answers.DONT_KNOW:
                self.text += 'Phasellus ac sem ornare, ANSWER_I_DONT_KNOW euismod tellus id, sagittis felis...'
            if q5_answer == Answers.YES and {2, 3}.issubset(q5_answer):
                self.text += 'Mauris viverra lobortis ante, eget faucibus felis pulvinar et...'
            if q5_answer == Answers.YES and {1, 4}.issubset(q5_answer):
                self.text += 'Fusce sem est, maximus ac efficitur in, accumsan eu libero...'
            else:
                self.text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...'

        return self.text
