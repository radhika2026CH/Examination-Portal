from django.contrib import admin
from .models import Course, Test, Mcq

@admin.register(Course)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'author']

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'test_name', 'course', 'duration']

@admin.register(Mcq)
class McqAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'option_1', 'option_2', 'option_3', 'option_4','answer', 'test']