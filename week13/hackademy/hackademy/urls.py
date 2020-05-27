from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('education/', include('education.urls')),
    path('admin/', admin.site.urls),
]
