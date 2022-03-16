from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('michaellevan/', include('michaellevanapp.urls')),
    path('admin/', admin.site.urls),
]