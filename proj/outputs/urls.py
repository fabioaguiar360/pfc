from django.urls import path
from .views import outputs

urlpatterns = [
    path('', outputs),
]