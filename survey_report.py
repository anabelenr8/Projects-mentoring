class Survey:
    def __init__(self):
        self.questions = {
            "Q1": {
                "question_text": "When you shop for clothing, which style best describes your preference?",
                "answers": {
                    1: "Casual and Comfortable",
                    2: "Elegant and Chic",
                    3: "Bohemian and Relaxed",
                    4: "Edgy and Experimental",
                    5: "None of the above"
                }
            },
            "Q2": {
                "question_text": "How do you usually choose the colors of your clothes?",
                "answers": {
                    1: "Bright and Vibrant",
                    2: "Neutral and Subdued",
                    3: "Dark and Muted",
                    4: "Pastel and Soft",
                    5: "I don't pay much attention to colors"
                }
            },
            "Q3": {
                "question_text": "Which clothing category do you shop for the most?",
                "answers": [
                    "Tops (Shirts, Blouses, T-shirts)",
                    "Bottoms (Pants, Skirts, Jeans)",
                    "Dresses and Jumpsuits",
                    "Outerwear (Jackets, Coats, Blazers)",
                    "Accessories (Bags, Shoes, Jewelry)",
                    "None of the above"
                ],
                "allow_multiple_answers": True
            },
            "Q4": {
                "question_text": "What's your clothing size?",
                "answers": {
                    "size": int,
                    "type": ["US", "EU", "UK"],
                    "prefer_not_to_answer": "I prefer not to answer"
                }
            },
            "Q5": {
                "question_text": "Are you familiar with Zara's sustainability efforts?",
                "answers": {
                    "Yes": {
                        "followup_question": "If Yes selected, which of the following sustainable practices do you know about? (Select all that apply)",
                        "options": {
                            1: "Use of organic materials",
                            2: "Recycling and upcycling initiatives",
                            3: "Reduction of water usage in production",
                            4: "I'm not sure"
                        }
                    },
                    "I don't know": "I have limited knowledge about it.",
                    "No": "No, I'm not aware of Zara's sustainability efforts."
                }
            },
        }


def calculate_recommendation(size):
    if size > 16:
        return "Consider choosing larger-sized clothing for comfort."
    else:
        return "Your clothing size is suitable."


# Predetermined answers
predetermined_answers = {
    'Q1': 2,
    'Q2': 2,
    'Q3': [3, 4, 5],
    'Q4': {"size": 14, "type": 'UK'},
    'Q5': "No"
}
report_text = ''

# for question_key, answer_value in predetermined_answers.items():
# Logic for generating the report text based on Q1 answer

if 'Q1' in predetermined_answers:
    q1_answer = predetermined_answers['Q1']
    if q1_answer == 1:
        report_text += 'Lorem ipsum 1. Question - ANSWER_1 dolor sit amet, consectetur adipiscing elit. Mauris sed ligula vitae tellus pellentesque vehicula nec eu velit. Curabitur luctus et nibh et ornare. Suspendisse non mattis lacus. Cras vitae mi ornare, euismod velit sit amet, iaculis tortor. In tempor purus sapien. \\ Donec tincidunt 1. Question - ANSWER_1 metus nec dui tristique malesuada. Praesent lectus nunc, accumsan vel justo in, imperdiet faucibus leo. Nullam efficitur massa nec turpis tincidunt, feugiat viverra erat rutrum. Aliquam eget auctor lectus, mollis blandit ipsum. Phasellus maximus finibus arcu a tincidunt.\n'
    elif q1_answer == 2:
        report_text += 'Lorem ipsum 1. Question - ANSWER_2 dolor sit amet, consectetur adipiscing elit. Ut et augue id leo egestas interdum in eu lectus. Aliquam vel finibus nisi. Vestibulum mattis sagittis lectus sed pulvinar. Sed aliquam felis tortor, sed scelerisque nibh cursus sit amet. Donec a sollicitudin nisi. Mauris non enim ac felis lobortis commodo. Sed laoreet tellus non felis rutrum, in hendrerit ipsum porta. Sed quis sem velit.\n'
    elif q1_answer == 3:
        report_text += 'Sed vel bibendum tortor. Proin a aliquet tortor. Vivamus rhoncus 1. Question - ANSWER_3 risus nec ultricies rutrum. Mauris bibendum lectus risus, non porttitor urna interdum quis. \\ Suspendisse quis risus scelerisque, 1. Question - ANSWER_3 feugiat augue nec, semper leo. Fusce euismod facilisis mi, tristique sollicitudin metus hendrerit non. Nulla ac sodales quam, sit amet finibus metus. Ut in felis tellus. Sed aliquet metus ullamcorper est vestibulum mattis. Cras nisi sem, euismod in egestas vel, ullamcorper ac sapien. In porttitor elementum faucibus.\n'
    elif q1_answer == 4 or 5 or 6:
        report_text += 'Mauris urna nunc, eleifend id sapien eget, tincidunt venenatis risus. Vestibulum imperdiet enim at nibh sodales, 1. Question - ANSWER_4 or ANSWER_5 or ANSWER_6 eget scelerisque odio finibus. \\ Nullam ut mi eget sapien accumsan iaculis. Vestibulum in maximus metus, 1. Question - ANSWER_4 or ANSWER_5 or ANSWER_6 vitae venenatis sapien. Nullam auctor odio vehicula, posuere elit in, ullamcorper lectus. Mauris pharetra dapibus congue. Suspendisse potenti.\n'

# Logic for generating the report text based on Q2 answer
if 'Q2' in predetermined_answers:
    q2_answer = predetermined_answers['Q2']
    if q2_answer == 1:
        report_text += 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus. Vestibulum imperdiet enim at nibh sodales, eget scelerisque odio finibus. Nullam ut mi eget sapien accumsan iaculis. Vestibulum in maximus metus, vitae venenatis sapien. Nullam auctor odio vehicula, posuere elit in, ullamcorper lectus. Mauris pharetra dapibus congue. 2. Question - ANSWER_1 or ANSWER_3 Suspendisse potenti.\n'
    elif q2_answer == 2:
        report_text += 'In nisl ligula, porttitor vel lobortis vel, commodo quis mi. Nullam sollicitudin odio ut felis tristique tempus. Cras sagittis auctor nulla 2. Question - ANSWER_2 or ANSWER_4 eget accumsan. Nam condimentum lacus non tortor auctor semper. \\ Suspendisse justo nisi, molestie quis purus sed, dapibus porta urna. Praesent leo massa, aliquet blandit eros at, consectetur vestibulum elit. Aliquam laoreet ex ex, et dapibus 2. Question - ANSWER_2 or ANSWER_4 ligula interdum a. Praesent quis libero arcu. Donec felis libero, tristique et sapien non, feugiat eleifend diam.\n'
    elif q2_answer == 3:
        report_text += 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus. Vestibulum imperdiet enim at nibh sodales, eget scelerisque odio finibus. Nullam ut mi eget sapien accumsan iaculis. Vestibulum in maximus metus, vitae venenatis sapien. Nullam auctor odio vehicula, posuere elit in, ullamcorper lectus. Mauris pharetra dapibus congue. 2. Question - ANSWER_1 or ANSWER_3 Suspendisse potenti.\n'
    elif q2_answer == 4:
        report_text += 'In nisl ligula, porttitor vel lobortis vel, commodo quis mi. Nullam sollicitudin odio ut felis tristique tempus. Cras sagittis auctor nulla 2. Question - ANSWER_2 or ANSWER_4 eget accumsan. Nam condimentum lacus non tortor auctor semper. \\ Suspendisse justo nisi, molestie quis purus sed, dapibus porta urna. Praesent leo massa, aliquet blandit eros at, consectetur vestibulum elit. Aliquam laoreet ex ex, et dapibus 2. Question - ANSWER_2 or ANSWER_4 ligula interdum a. Praesent quis libero arcu. Donec felis libero, tristique et sapien non, feugiat eleifend diam.\n'
    elif q2_answer == 5:
        report_text += 'Mauris urna nunc, eleifend id sapien eget, 2. Question - ANSWER_1 or ANSWER_3 tincidunt venenatis risus. Vestibulum imperdiet enim at nibh sodales, eget scelerisque odio finibus. Nullam ut mi eget sapien accumsan iaculis. Vestibulum in maximus metus, vitae venenatis sapien. Nullam auctor odio vehicula, posuere elit in, ullamcorper lectus. Mauris pharetra dapibus congue. 2. Question - ANSWER_1 or ANSWER_3 Suspendisse potenti.\n'

# Logic for generating the report text based on Q3 answer
if 'Q3' in predetermined_answers:
    q3_answers = predetermined_answers['Q3']
    if set(q3_answers) == {1, 3, 4}:
        report_text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sollicitudin leo in 3. Question - ANSWER_4, ANSWER_3 and ANSWER_1 lectus cursus tincidunt. Nullam dapibus tincidunt libero nec volutpat. \\ Cras sit amet massa a turpis malesuada ornare vitae sed arcu. Maecenas eleifend rutrum augue, eget imperdiet sem gravida sed. Vestibulum vel libero consectetur, 3. Question - ANSWER_4, ANSWER_3 and ANSWER_1 pellentesque lacus nec, facilisis nisl. Phasellus faucibus lobortis tincidunt. Duis tristique congue bibendum. \\ Morbi semper cursus felis et consequat. Nulla posuere, quam eget pulvinar 3. Question - ANSWER_4, ANSWER_3 and ANSWER_1 dignissim, odio sem euismod leo, at ornare purus massa quis sapien. Aliquam eget libero nec lectus placerat congue. Aenean nec tortor a ligula aliquam pharetra. Aenean et magna enim.\n'
    elif set(q3_answers) == {2, 5}:
        report_text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum dictum, dui non auctor tristique, odio sem 3. Question - ANSWER_2 and ANSWER_5 convallis lacus, non gravida libero erat id justo. Praesent in varius nisi. Phasellus suscipit elit sit amet aliquam tincidunt. \\ In pellentesque gravida risus, et 3. Question - ANSWER_2 and ANSWER_5 rhoncus quam. Vestibulum ac risus nulla. Phasellus iaculis interdum pulvinar. Vivamus sit amet sagittis risus. Morbi ut pellentesque sapien.\n'
    elif set(q3_answers) & {1, 3, 4}:
        report_text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras viverra luctus nunc, non ultrices mauris molestie vitae. Sed gravida purus finibus 3. Question - ANSWER_4, ANSWER_3 or ANSWER_1 efficitur congue. Vestibulum magna urna, volutpat vitae auctor non, pharetra vel leo. \\ Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum elementum sagittis tortor, vel porta leo tristique ac. Phasellus ac metus est. 3. Question - ANSWER_4, ANSWER_3 or ANSWER_1 Aenean vel malesuada ex, nec rutrum justo. Sed ultricies venenatis mauris, in pharetra ante vulputate nec. Proin viverra convallis augue elementum volutpat.\n'
    else:
        report_text += 'Consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \\ Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n'

# Logic for generating the report text based on Q4 answer
if 'Q4' in predetermined_answers:
    q4_answer = predetermined_answers['Q4']
    if isinstance(q4_answer, dict) and 'size' in q4_answer:
        size = q4_answer['size']
        recommendation = calculate_recommendation(size)
        report_text += f"Your clothing size is {size}. {recommendation}\n"

# Logic for generating the report text based on Q5 answer
if 'Q5' in predetermined_answers:
    q5_answer = predetermined_answers['Q5']
    if q5_answer == "No":
        report_text += 'Nam maximus et massa laoreet congue. In facilisis egestas neque. Nullam ac euismod nibh. ANSWER_NO Aenean pulvinar lacinia ligula, nec lobortis magna accumsan sed.'
    elif q5_answer == "I don't know":
        report_text += 'Phasellus ac sem ornare, ANSWER_I_DONT_KNOW euismod tellus id, sagittis felis. Nullam viverra est nibh, et dignissim elit tincidunt nec. Integer vel dolor aliquam, eleifend metus in, tincidunt erat. Nam id facilisis tortor.'
    elif q5_answer == "Yes" and {2, 3}:
        report_text += 'Mauris viverra lobortis ante, eget faucibus felis pulvinar et. Suspendisse urna diam, ANSWER_YES and ANSWER_YES_CHOICE_2, ANSWER_YES_CHOICE_3 elementum nec tincidunt ornare, convallis condimentum nisi.'
    elif q5_answer == "Yes" and {1, 4}:
        report_text += 'Fusce sem est, maximus ac efficitur in, accumsan eu libero. Praesent facilisis, augue at pretium malesuada, ANSWER_YES and ANSWER_YES_CHOICE_1, ANSWER_YES_CHOICE_4 erat eros eleifend velit, at iaculis nunc nisi nec odio. Ut consequat ac metus a bibendum. Donec venenatis euismod eros ac dignissim. Donec dictum odio a augue tincidunt interdum.'
    else:
        report_text += 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque sed scelerisque nulla, at mattis mauris. Vestibulum dignissim viverra nulla quis tempus. (Any other case) Donec finibus nisl sapien, sed auctor elit sodales ac. Nulla dictum ante ante, eget maximus mi efficitur nec.'

survey = Survey
report = report_text

survey_report = survey and report

print(survey_report)
