from rest_framework import serializers


class RecyclingMaterialSerializer(serializers.Serializer):
    answer = serializers.ChoiceField(choices=['yes', 'limited knowledge', 'not_aware'])
    choices = serializers.ChoiceField(
        choices=[
            'organic_materials',
            'recycling_materials',
            'reuse_water',
            'not_sure']
    )


class TypeAndSizeSerializer(serializers.Serializer):
    size = serializers.IntegerField()
    type = serializers.ChoiceField(
        choices=[
            'type_uk',
            'type_us',
            'type_eu']
    )


class SurveySerializer(serializers.Serializer):
    your_style = serializers.ChoiceField(
        choices=[
            'casual_and_comfortable',
            'elegant_and_chic',
            'bohemian_and_relaxed',
            'edgy_and_experimental',
            'none_of_the_above']
    )
    colour_palette = serializers.ChoiceField(
        choices=[
            'bright_and_vibrant',
            'neutral_and_subdued',
            'dark_and_muted',
            'pastel_and_soft',
            'I_dont_pay_much_attention_to_colors']
    )
    shopping_category = serializers.ListField(
        child=serializers.ChoiceField(
            choices=
            ['tops',
             'bottoms',
             'accessories',
             'shoes']
        ),
        allow_empty=False
    )
    type_and_size = TypeAndSizeSerializer()

    preference_on_recycling_materials = RecyclingMaterialSerializer()
