from django.urls import path
from . import views
urlpatterns = [
    path('McqDetail/<int:pk>', views.McqDetails.as_view()),
    path('McqRegister/', views.McqDetails.as_view()),
    path('McqList/', views.McqList.as_view()),

    path('TestDetail/<int:pk>', views.TestDetails.as_view()),
    path('TestList/', views.TestList.as_view()),
    path('TestRegister/', views.TestDetails.as_view()),
    
    path('CourseList/', views.CourseList.as_view()),
    path('CourseDetail/<int:pk>', views.CourseDetails.as_view()),
    path('CourseRegister/', views.CourseDetails.as_view())

]