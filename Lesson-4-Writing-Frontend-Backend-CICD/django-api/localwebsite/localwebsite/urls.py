from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cloudskills/', include('cloudskillsapp.urls')),
    path('admin/', admin.site.urls),
]