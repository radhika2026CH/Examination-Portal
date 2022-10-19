from multiprocessing import context
from rest_framework import serializers
from .models import Course, Test, Mcq


class CourseSerializer(serializers.Serializer):
    course_name = serializers.CharField(max_length=256)
    author = serializers.CharField(max_length=256)

    def create(self, valid_data):
        return Course.objects.create(**valid_data)

    def update(self, instance, validated_data):
        instance.course_name = (
            validated_data.get("course_name", instance.course_name),
        )
        instance.author = validated_data.get(
            "author", instance.author
        )
        instance.save()
        return instance

    class Meta:
        model = Course
        fields = "__all__"

class TestSerializer(serializers.Serializer):
    test_name = serializers.CharField(max_length=256)
    course = CourseSerializer(read_only=True)
    duration = serializers.DurationField()

    def create(self, valid_data):
        request = self.context["request"]
        course = request.data.get("course")
        test_obj = Test(**valid_data)
        test_obj.course_id = course
        print("TESTTTTTT ", test_obj)
        test_obj.save()
        return test_obj

    def update(self, instance, validated_data):
        instance.test_name = validated_data.get("test_name", instance.test_name)
        instance.duration = validated_data.get("duration", instance.duration)
        instance.save()
        return instance

    class Meta:
        model = Test
        fields = "__all__"


class McqSerializer(serializers.Serializer):
    question = serializers.CharField()
    option_1 = serializers.CharField()
    option_2 = serializers.CharField()
    option_3 = serializers.CharField()
    option_4 = serializers.CharField()
    answer = serializers.CharField()
    test = TestSerializer(read_only=True)

    def create(self, valid_data):
        request = self.context["request"]
        test = request.data.get("test")
        test_obj = Mcq(**valid_data)
        test_obj.test_id = test
        test_obj.save()
        return test_obj

    def update(self, instance, validated_data):
        instance.question = validated_data.get("question", instance.question)
        instance.option_1 = validated_data.get("option_1", instance.option_1)
        instance.option_2 = validated_data.get("option_2", instance.option_2)
        instance.option_3 = validated_data.get("option_3", instance.option_3)
        instance.option_4 = validated_data.get("option_4", instance.option_4)
        instance.answer = validated_data.get("answer", instance.answer)
        test = validated_data.get("test", instance.test)
        instance.save()
        return instance