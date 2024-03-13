from rest_framework import serializers


class ChoiceSerializer(serializers.Serializer):
    answer = serializers.CharField()
    choices = serializers.CharField()


class UserAnswersSerializer(serializers.Serializer):
    Q1 = serializers.CharField()
    Q2 = serializers.CharField()
    Q3 = serializers.ListField(child=serializers.CharField())
    Q4 = serializers.ListField(child=serializers.CharField())
    Q5 = ChoiceSerializer()

    def validate(self, data):
        """
        Check that all questions have been answered.
        """
        missing_answers = []
        for question, answer in data.items():
            # Assuming that an empty string is not a valid answer
            if answer in (None, '', [], {}):
                missing_answers.append(question)

        if missing_answers:
            raise serializers.ValidationError(
                f"Missing answers for: {', '.join(missing_answers)}."
            )

        return data
