from enum import unique
from statistics import mode
from wsgiref.validate import validator
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from rest_framework.response import Response

def answer_key_validator(option):
    if option in ["a", "b", "c", "d"]:
        return option
    else:
        raise ValidationError("Invalid value")


class Course(models.Model):
    course_name = models.CharField(max_length=256, null=False, blank=False, unique=True)
    creater_name = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.course_name


class Test(models.Model):
    test_name = models.CharField(max_length=256, null=False, blank=False, unique=True)
    test_duration = models.DurationField(null=False, blank=False)
    fk_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name


class Question(models.Model):
    question = models.TextField(max_length=600, null=False, blank=False, unique=True)
    option_a = models.TextField(max_length=600, null=False, blank=False)
    option_b = models.TextField(max_length=600, null=False, blank=False)
    option_c = models.TextField(max_length=600, null=False, blank=False)
    option_d = models.TextField(max_length=600, null=False, blank=False)
    answer = models.TextField(max_length=600, validators=[answer_key_validator], null = True)
    fk_test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class StudentCourse(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    def __str__(self):
        return (str(self.course))

class TestAppeared(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    test = models.ForeignKey(Test, on_delete = models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    score = models.IntegerField(default = 0)

    def __str__(self):
        return (str(self.test))

class SelectedAnswers(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    test = models.ForeignKey(Test, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    selected_answer = models.TextField(max_length=600)

    def __str__(self):
        return (str(self.question))