from django.urls import path
from .views import inputs

urlpatterns = [
    path('', inputs),
]