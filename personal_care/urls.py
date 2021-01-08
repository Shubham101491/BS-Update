from django.urls import path
from . import views

urlpatterns = [
    path('care/', views.care, name='care'),
    # path('single/', views.single, name='single'),
]
