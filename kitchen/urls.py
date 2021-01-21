from django.urls import path
from . import views

urlpatterns = [
    path('water_beverages/', views.water_beverages, name='water_beverages'),
    path('product/<int:id>', views.product, name='product'),
]
