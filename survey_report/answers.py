class Answers:
    # Answers for question 1
    CASUAL_AND_COMFORTABLE = "Casual and Comfortable"
    ELEGANT_AND_CHIC = "Elegant and Chic"
    BOHEMIAN_AND_RELAXED = "Bohemian and Relaxed"
    EDGY_AND_EXPERIMENTAL = "Edgy and Experimental"
    NONE_OF_THE_ABOVE = "None of the above"

    # Answers for question 2
    BRIGHT_AND_VIBRANT = "Bright and Vibrant"
    NEUTRAL_AND_SUBDUED = "Neutral and Subdued"
    DARK_AND_MUTED = "Dark and Muted"
    PASTEL_AND_SOFT = "Pastel and Soft"
    NO_ATTENTION = "I don't pay much attention to colors"

    # Answers for question 3
    TOPS = "Tops (Shirts, Blouses, T-shirts)"
    BOTTOMS = "Bottoms (Pants, Skirts, Jeans)"
    DRESSES_AND_JUMPSUITS = "Dresses and Jumpsuits"
    ACCESSORIES = "Accessories (Bags, Shoes, Jewelry)"
    SHOES = "shoes"

    # Answers for question 4
    size = int
    TYPE = ["US", "EU", "UK"]
    PREFER_NOT_TO_ANSWER = "I prefer not to answer"

    # Answers for question 5
    YES = {
        "followup_question": "If Yes selected, which of the following sustainable practices do you know about? (Select all that apply)",
        "options": {
            1: "Use of organic materials",
            2: "Recycling and upcycling initiatives",
            3: "Reduction of water usage in production",
            4: "I'm not sure"
        }
    }
    DONT_KNOW = "I have limited knowledge about it."
    NO = "No, I'm not aware of Zara's sustainability efforts."
