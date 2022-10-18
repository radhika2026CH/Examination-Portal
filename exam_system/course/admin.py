from django.contrib import admin
from .models import Course, Test

@admin.register(Course)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'author']

