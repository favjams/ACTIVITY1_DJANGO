from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('productdetails/', views.productdetails, name='productdetails'),
]