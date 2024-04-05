from rest_framework import serializers
from store.reports.generate.answers import Answers


class RecyclingMaterialSerializer(serializers.Serializer):
    answer = serializers.ChoiceField(
        choices=[Answers.YES,
                 Answers.DONT_KNOW,
                 Answers.NO])

    choices = serializers.ChoiceField(
        choices=[
            Answers.CHOICE_ORGANIC,
            Answers.CHOICE_RECYCLING,
            Answers.CHOICE_WATER,
            Answers.CHOICE_NOT_SURE]
    )


class TypeAndSizeSerializer(serializers.Serializer):
    size = serializers.IntegerField()
    type = serializers.ChoiceField(
        choices=[
            Answers.TYPE_UK,
            Answers.TYPE_US,
            Answers.TYPE_EU]
    )


class SurveySerializer(serializers.Serializer):
    your_style = serializers.ChoiceField(
        choices=[
            Answers.CASUAL_AND_COMFORTABLE,
            Answers.ELEGANT_AND_CHIC,
            Answers.BOHEMIAN_AND_RELAXED,
            Answers.EDGY_AND_EXPERIMENTAL,
            Answers.NONE_OF_THE_ABOVE]
    )
    colour_palette = serializers.ChoiceField(
        choices=[
            Answers.BRIGHT_AND_VIBRANT,
            Answers.NEUTRAL_AND_SUBDUED,
            Answers.DARK_AND_MUTED,
            Answers.PASTEL_AND_SOFT,
            Answers.NO_ATTENTION]
    )
    shopping_category = serializers.ListField(
        child=serializers.ChoiceField(
            choices=
            [Answers.TOPS,
             Answers.BOTTOMS,
             Answers.ACCESSORIES,
             Answers.SHOES,
             Answers.DRESSES_AND_JUMPSUITS]
        ),
        allow_empty=False
    )
    type_and_size = TypeAndSizeSerializer()

    preference_on_recycling_materials = RecyclingMaterialSerializer()
