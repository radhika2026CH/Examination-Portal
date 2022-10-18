from django.db import models
from django.core.exceptions import ValidationError

class Course(models.Model):
    course_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    author = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.course_name

class Test(models.Model):
    test_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    duration = models.DurationField(null=False, blank=False)


def answer_key_validator(option):
        if option in ["option_1", "option_2", "option_3", "option_4"]:
            return option
        else:
            raise ValidationError("This option does not exists")


class Mcq(models.Model):
    
    question = models.TextField(null=False, blank=False, unique=True)
    option_1 = models.TextField(null=False, blank=False)
    option_2 = models.TextField(null=False, blank=False)
    option_3 = models.TextField(null=False, blank=False)
    option_4 = models.TextField(null=False, blank=False)
    answer = models.CharField(max_length = 200, validators =[answer_key_validator])

