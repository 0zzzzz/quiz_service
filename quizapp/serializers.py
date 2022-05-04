from rest_framework import serializers
from quizapp.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Cериализатор для товаров"""
    class Meta:
        model = Question
        fields = '__all__'

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.question_id = validated_data.get('question_id', instance.question_id)
        instance.question_text = validated_data.get('question_text', instance.question_text)
        instance.question_answer = validated_data.get('question_answer', instance.question_answer)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

