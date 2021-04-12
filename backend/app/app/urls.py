from django.contrib import admin
from django.urls import path
from url_checker.views import check_url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('url_checker', check_url),
]