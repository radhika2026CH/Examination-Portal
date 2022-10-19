from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student.urls')),
    path('staff/', include('staff.urls')),
    path('course/', include('course.urls'))
      
]
