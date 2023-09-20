from django.urls import path
from . import views
from .views import contact, success

urlpatterns = [
    path("", views.index, name="index"),
    path("service", views.service, name="services"),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
   
]