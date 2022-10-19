from django.urls import path
from . import views
urlpatterns = [
    path('StudentDetail/<int:pk>', views.StudentDetail.as_view()),
    path('StudentList/', views.StudentRegistration.as_view()),
    path('StudentRegister/', views.StudentRegistration.as_view()),  
    path('login/', views.UserLogin.as_view()),
    path('logout/', views.logoutUser),
    
]
