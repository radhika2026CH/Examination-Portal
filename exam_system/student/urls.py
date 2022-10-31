from django.urls import path
from . import views
urlpatterns = [
    # path('StudentDetail/<int:pk>', views.StudentDetail.as_view()),
    # path('StudentList/', views.StudentRegistration.as_view()),
    path('user-register/', views.UserRegister.as_view()), 
    path('login/', views.UserLogin.as_view()),
    path('logout/', views.logoutUser),
    path('students-detail/', views.AllStudent.as_view()), 
    path('staffs-detail/', views.AllStaff.as_view()),
    path('detail/', views.UserDetail.as_view()),
    path('/user-by-JWT/', views.UserByJWT.as_view()),

]
