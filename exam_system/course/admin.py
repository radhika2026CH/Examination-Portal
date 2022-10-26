from django.contrib import admin
from .models import Course, Test, Question, StudentCourse, TestAppeared, SelectedAnswers

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id' ,'course_name', 'creater_name']

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['id' ,'test_name', 'test_duration', 'fk_course']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id' ,'question', 'answer', 'option_a', 'option_b', 'option_c', 'option_d', 'fk_test']

@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'course_id']
    
@admin.register(TestAppeared)
class TestAppearedAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'test_id', 'start_time', 'end_time', 'score']

@admin.register(SelectedAnswers)
class SelectedAnswersAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'test_id', 'question_id', 'selected_answer']