from django.contrib import admin
from django.urls import path
from core.views import home, download_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('download_report/', download_report, name='download_report'),
]
