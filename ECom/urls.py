from django.urls import path
from .views import TestView

urlpatterns = [
    path('', TestView, name='test-list'),
]