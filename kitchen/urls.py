from django.urls import path
from . import views

urlpatterns = [
    path('water_beverages/',views.water_beverages,name='water_beverages'),
    path('single/', views.single, name='single'),
]