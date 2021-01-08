from django.urls import path
from . import views

urlpatterns = [
    path('care/', views.care, name='care'),

]
