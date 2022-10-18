from django.urls import path
from . import views
urlpatterns = [
    path('StudentDetail/<int:pk>', views.StudentDetail.as_view()),
    path('StudentList/', views.StudentList.as_view()),
    path('StudentRegister/', views.StudentDetail.as_view()),
    
]
