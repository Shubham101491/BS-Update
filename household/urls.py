from django.urls import path
from . import views

urlpatterns = [
    path('hold/', views.hold, name='hold'),
]