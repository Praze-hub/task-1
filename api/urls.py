from django.urls import path
from .views import get_info

urlpatterns = [
    path('info/', get_info, name='get_info'),
]