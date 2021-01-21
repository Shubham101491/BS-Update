from django.urls import path
from . import views

urlpatterns = [
    path('shipping/', views.shipping, name='shipping'),
    path('terms/', views.terms, name='terms'),
    path('faqs/', views.faqs, name='faqs'),
    path('wishlist/', views.wishlist, name='wishlist'),
    
    path('offer/', views.offer, name='offer'),


    # Kitchen Data
    path('single_detail_1/<int:id>', views.single_detail_1, name='single_detail_1'),
    # Personal Data
    path('single_detail_2/<int:id>', views.single_detail_2, name='single_detail_2'),
    # HouseHold Data
    path('single_detail_3/<int:id>', views.single_detail_3, name='single_detail_3'),
    # Special Data
    # path('single_detail_4/<int:id>', views.single_detail_4, name='single_detail_4'),

]
