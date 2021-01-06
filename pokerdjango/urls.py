from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pokersociale.urls')),
    path('admin/', admin.site.urls),
]
