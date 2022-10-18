from django.urls import path
from . import views
urlpatterns = [
    path('StaffDetail/<int:pk>', views.StaffDetail.as_view()),
    path('StaffList/', views.StaffList.as_view()),
    path('StaffRegister/', views.StaffDetail.as_view()),
    
]