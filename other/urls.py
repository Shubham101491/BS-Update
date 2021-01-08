from django.urls import path
from . import views

urlpatterns = [
    path('shipping/', views.shipping, name='shipping'),
    path('offer/', views.offer, name='offer'),
    path('wishlist/', views.wishlist, name='wishlist'),
    # path('single/', views.single, name='single'),
    path('terms/', views.terms, name='terms'),
    path('faqs/', views.faqs, name='faqs'),
]