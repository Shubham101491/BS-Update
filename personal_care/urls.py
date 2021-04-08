from django.urls import path
from . import views

urlpatterns = [
    path('care/', views.care, name='care'),
    path('product/<int:id>', views.product, name='product'),
]
