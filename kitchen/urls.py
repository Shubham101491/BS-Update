from django.urls import path
from . import views

urlpatterns = [
    path('water_beverages/',views.water_beverages,name='water_beverages'),
    # path('kitch_prod/<int:id>',views.kitch_prod,name='kitch_prod'),
]