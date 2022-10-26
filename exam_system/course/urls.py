# from django.urls import path
# from . import views
# urlpatterns = [
# #     path('McqDetail/<int:pk>', views.McqDetails.as_view()),
# #     path('McqRegister/', views.McqDetails.as_view()),
# #     path('McqList/', views.McqList.as_view()),

# #     path('TestDetail/<int:pk>', views.TestDetails.as_view()),
# #     path('TestList/', views.TestList.as_view()),
# #     path('TestRegister/', views.TestDetails.as_view()),
    
# #     path('CourseList/', views.CourseList.as_view()),
# #     path('CourseDetail/<int:pk>', views.CourseDetails.as_view()),
# #     path('CourseRegister/', views.CourseDetails.as_view())

# ]
from django.urls import path
from course import views

urlpatterns = [ 
    # ! Course URLS 
    path('course/course-list/', views.AllCourses.as_view()),
    path('course/update-course/<int:pk>', views.CourseDetail.as_view()),
    path('course/delete-course/<int:pk>', views.CourseDetail.as_view()),
    path('course/create-course/', views.CourseDetail.as_view()),
    path('course/detail-course/<int:pk>', views.CourseDetail.as_view()),
    # ! Test URLS
    path('test/test-list/', views.AllTests.as_view()),
    path('test/detail-test/<int:pk>', views.TestDetail.as_view()),
    path('test/update-test/<int:pk>', views.TestDetail.as_view()),
    path('test/delete-test/<int:pk>', views.TestDetail.as_view()),
    path('test/create-test/', views.TestDetail.as_view()),
    path('test/test-list-by-course/<int:pk>', views.AllTestsByCourseId.as_view()),
    #  ! Question URLS
    path('question/question-list/', views.AllQuestion.as_view()),
    path('question/detail-question/<int:pk>', views.QuestionDetail.as_view()),
    path('question/update-question/<int:pk>', views.QuestionDetail.as_view()),
    path('question/delete-question/<int:pk>', views.QuestionDetail.as_view()),
    path('question/create-question/', views.QuestionDetail.as_view()),
    path('questions/ques-list-by-test/<int:pk>', views.AllQuestionsByTestId.as_view()),
    
    path('student-course/add-student-course/', views.StudentCourseView.as_view()),
    path('student-course/get-student-course/', views.StudentCourseView.as_view()),
    path('student-course/delete-student-course/<int:pk>', views.StudentCourseView.as_view()),
    
    path('student-test/add-student-test/', views.TestAppearedView.as_view()),
    path('student-test/get-student-test/', views.TestAppearedView.as_view()),

    path('student-answer/add-student-answer/', views.SelectedAnswersView.as_view()),
    path('student-answer/get-student-answer/<int:pk>', views.SelectedAnswersView.as_view()),

]