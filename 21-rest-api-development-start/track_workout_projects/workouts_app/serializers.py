from rest_framework import serializers

from .models import Exercise

# a "serializer" is something that knows how to package data for transport
class ExerciseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    exercise_type = serializers.ChoiceField(choices=Exercise.EXERCISE_TYPES)

    def create(self, validated_data):
        return Exercise.objects.create(**validated_data)