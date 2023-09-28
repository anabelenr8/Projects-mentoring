from .answers import Answers

# Predetermined answers
predetermined_answers = {
    'Q1': Answers.ELEGANT_AND_CHIC,
    'Q2': Answers.PASTEL_AND_SOFT,
    'Q3': [Answers.TOPS, Answers.BOTTOMS, Answers.ACCESSORIES],
    'Q4': {Answers.size: 14, Answers.TYPE: "UK"},
    'Q5': Answers.NO
}


class Survey:
    def __init__(self, Q1, Q2, Q3, Q4, Q5):
        self.Q1 = Q1
        self.Q2 = Q2
        self.Q3 = Q3
        self.Q4 = Q4
        self.Q5 = Q5


user_submitted_survey = Survey(**predetermined_answers)
