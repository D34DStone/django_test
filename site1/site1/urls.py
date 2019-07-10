from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('simple_api/', include('simple_api.urls')),
    path('admin/', admin.site.urls),
]